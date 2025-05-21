# crypto_tools.py
import requests

def get_price_info(token_id):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={token_id}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return f"Цена {token_id}: ${data[token_id]['usd']}"

def get_market_info(token_id):
    url = f"https://api.coingecko.com/api/v3/coins/{token_id}"
    response = requests.get(url)
    data = response.json()
    market_cap = data['market_data']['market_cap']['usd']
    rank = data['market_cap_rank']
    return f"Рыночная капитализация: ${market_cap}, Ранг: #{rank}"

def get_crypto_news():
    url = "https://cryptopanic.com/api/v1/posts/?auth_token=demo&public=true"
    response = requests.get(url)
    data = response.json()
    news = [item['title'] for item in data['results'][:3]]
    return "\n".join(news)

def find_token_id(symbol):
    url = "https://api.coingecko.com/api/v3/coins/list"
    response = requests.get(url)
    tokens = response.json()
    symbol_lower = symbol.lower()
    for token in tokens:
        if token['symbol'].lower() == symbol_lower or token['id'].lower() == symbol_lower or token['name'].lower() == symbol_lower:
            return token['id']
    return None
