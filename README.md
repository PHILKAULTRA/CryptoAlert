# CryptoAlert
This is a python program that sends alerts about top 20 cryptos' values to your telegram bot every minute

Before running the script, you'll need to obtain a Telegram bot token and chat ID. Here are the steps to get them:

1 - Open the Telegram app and search for the "BotFather" bot.

2 - Send a message "/start" to BotFather to start the bot.

3 - Send a message "/newbot" to BotFather to create a new bot. Follow the instructions and enter a name and username for your bot.

4 - BotFather will send you a bot token. Copy the token and save it somewhere.

5 - Open the Telegram app and search for your bot by username.

6 - Send a message to your bot.

7 - Open the following URL in your web browser, replacing "BOT_TOKEN" with your bot token and "CHAT_ID" with the chat ID you received from your bot: https://api.telegram.org/botBOT_TOKEN/getUpdates

8 - Look for the "chat" object in the JSON response and find the "id" field. This is your chat ID.

![alt text](https://github.com/PHILKAULTRA/CryptoAlert/blob/main/Bot.png?raw=true)
