# app.py
import streamlit as st
from dotenv import load_dotenv
import os
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from blockchain import store_on_chain
from crypto_tools import get_price_info, get_market_info, get_crypto_news, find_token_id

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="AI Multi-Assistant")
st.title("🤖 Выберите режим AI")

mode = st.sidebar.radio("Режим", ["AI Конституция", "AI Crypto Assistant"])

llm = ChatOpenAI(openai_api_key=openai_key, model="gpt-4-1106-preview")

if mode == "AI Конституция":
    st.header("📜 AI Assistant по Конституции РК (On-Chain)")

    uploaded_files = st.file_uploader("Загрузите PDF-документы", accept_multiple_files=True)

    if uploaded_files:
        all_text = ""
        for file in uploaded_files:
            reader = PdfReader(file)
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    all_text += text

        text_splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=50)
        texts = text_splitter.split_text(all_text)

        embeddings = OpenAIEmbeddings(openai_api_key=openai_key)
        db = Chroma.from_texts(texts, embedding=embeddings, persist_directory="db")
        db.persist()
        retriever = db.as_retriever(search_kwargs={"k": 3})

        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="map_reduce",
            retriever=retriever,
            return_source_documents=False
        )

        query = st.text_input("Задай вопрос:")
        if query:
            try:
                result = qa_chain.run(query)
                st.write("Ответ:", result)

                store_on_chain(query, result)
                st.success("Сохранено в смарт-контракте!")
            except Exception as e:
                st.error(f"Ошибка: {str(e)}")

elif mode == "AI Crypto Assistant":
    st.header("🪙 AI Crypto Assistant")

    symbol = st.text_input("Введите название токена (например: bitcoin, eth, sol):")
    if symbol:
        token_id = find_token_id(symbol)
        if not token_id:
            st.error("Монета не найдена. Попробуйте другое имя.")
            st.stop()

        try:
            price = get_price_info(token_id)
            market = get_market_info(token_id)
            news = get_crypto_news()

            st.subheader("📊 Рыночная информация")
            st.write(price)
            st.write(market)

            st.subheader("📰 Последние новости")
            st.write(news)

            prompt = f"Расскажи про {token_id}. Его цена {price}. Инфо: {market}. Новости: {news}."
            response = llm.invoke(prompt)
            st.subheader("🤖 Ответ AI")
            st.write(response)
        except Exception as e:
            st.error(f"Ошибка при получении данных: {str(e)}")
