# 🇰🇿 AI Constitution Assistant (Kazakhstan)

This project is an AI-powered assistant built with **Streamlit**, **LangChain**, and **OpenAI GPT-4**, capable of answering questions about the **Constitution of the Republic of Kazakhstan** and analyzing **crypto market data**.

---

## 🚀 Features

- Upload and analyze any PDF version of the Constitution
- Ask natural language questions (e.g. "What does Article 2 say?")
- Store Q&A on-chain using Ethereum (Sepolia) smart contract
- Switch to Crypto Assistant mode and get:
  - Live crypto prices
  - Market cap & rankings
  - Latest news from CryptoPanic
- Uses GPT-4 for extended context (up to 128K tokens)
- Optimized to reduce API usage cost with chunking and retrieval limits

---

## 📂 Project Structure

```
ai-assistant/
├── app.py                 # Main Streamlit application
├── blockchain.py          # Handles blockchain storage
├── crypto_tools.py        # Crypto price/news utilities
├── requirements.txt       # Python dependencies
├── .env.example           # Template for environment variables
├── smart_contract/
│   └── abi.json           # ABI for deployed contract
├── README.md              # This file
└── db/                    # Vector store (auto-created, gitignored)
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/ai-assistantkz.git
cd ai-assistantkz
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a file named `.env` in the root of the project:

```
OPENAI_API_KEY=your-openai-key
WEB3_PROVIDER=https://sepolia.infura.io/v3/your-project-id
CONTRACT_ADDRESS=your-deployed-contract-address
PRIVATE_KEY=your-wallet-private-key
ACCOUNT_ADDRESS=your-wallet-address
```

---

## ▶️ Run the assistant

```
streamlit run app.py
```

Then open `http://localhost:8501` in your browser.

---

## 💸 Cost Control (Important)

If you're using GPT-4 (`gpt-4-1106-preview`), it's expensive. To reduce costs:

- Limit chunk size: `chunk_size=300`
- Use top K documents: `search_kwargs={"k": 2}`
- Set `max_tokens=800` for shorter responses

You can change these settings in `app.py`.

---

## 🪙 Supported Tokens for Crypto Assistant

You can enter names, symbols or IDs:
- `bitcoin`, `btc`, `Bitcoin`
- `solana`, `sol`, `Solana`
- `dogecoin`, `doge`, etc.

The app uses `find_token_id()` to locate any coin listed on [CoinGecko](https://coingecko.com).

---

## 📄 Example Questions

### Constitution:
- What is stated in Article 1?
- What rights are guaranteed to citizens?
- How is the Parliament structured?

### Crypto:
- What's the price of Ethereum?
- Give me the market rank of Solana
- Any latest news on Bitcoin?

---

## 🧠 Made by

Developed by Malika Syzdykova | Astana IT University  
Group: SE-2322
