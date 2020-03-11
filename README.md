# Telegram eInk Bot

## Summary
This hobby project was created to be able so send messages from a Telegram bot and display it on the eInk Hat on a Raspberry Pi. The following hardware is what I have used for mine:
- <a href="https://www.amazon.com/gp/product/B0751H7WB7/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1" target="_blank">Waveshare 2.7" Tri-color Hat</a>
- <a href="https://www.adafruit.com/product/3775" target="_blank">Raspberry Pi 3 B+</a>

### Configuring the bot
You will have to have to have a <a href="https://core.telegram.org/bots" target="_blank">Telegram Bot</a> <a href="https://www.siteguarding.com/en/how-to-get-telegram-bot-api-token" target="_blank">API Token</a> to use in the configuration file. Once you have your API Token, rename `config.ini_example` to `config.ini` and enter your API Key where the example key is under `bot_api_key`.

## Status
The current functionality allows someone to send it some messages with specific commands. Raspberry Pi will display different results based on the input. In the future, the logic for commands will be abstracted and given integration with the buttons as well as Smart Bulbs/Smart LED Strips.
