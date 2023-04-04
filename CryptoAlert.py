import requests
import time

# Replace YOUR_BOT_TOKEN and YOUR_CHAT_ID with your actual values
bot_token = "YOUR_BOT_TOKEN"
chat_id = "YOUR_CHAT_ID"

# Fetch the top 20 cryptocurrencies by market capitalization from the CoinGecko API
def fetch_top_20():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=20&page=1&sparkline=false"
    response = requests.get(url)
    data = response.json()
    return data

# Calculate the percentage change in the value of a cryptocurrency in the past 24 hours
def calc_percentage_change(current_price, previous_price):
    return round(((current_price - previous_price) / previous_price) * 100, 2)

# Send a message to the Telegram bot
def send_message(message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}"
    response = requests.get(url)
    return response.json()

# Main loop
while True:
    data = fetch_top_20()
    message = "Top 20 cryptocurrencies by market cap:\n"
    for i, crypto in enumerate(data, start=1):
        name = crypto["name"]
        symbol = crypto["symbol"].upper()
        price = crypto["current_price"]
        if i == 1:
            prev_price = price
        pct_change = calc_percentage_change(price, prev_price)
        if pct_change > 0:
            change_indicator = "📈"
        elif pct_change < 0:
            change_indicator = "📉"
        else:
            change_indicator = "➡️"
        message += f"{i}. {name} ({symbol}): ${price:.2f} ({change_indicator}{pct_change}%)\n"
        prev_price = price
    send_message(message)
    time.sleep(60)
