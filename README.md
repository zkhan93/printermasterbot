# Telegram Printer Bot

## Overview

This project is a Telegram bot that allows users to print documents directly from their Telegram chat. The bot is written in Python and runs as a Docker container. It connects to a printer via USB and accepts any file type sent in a Telegram chat.

## Requirements

- Docker
- Python
- A printer

## Usage

1. Build the Docker image:
```
docker build -t printer-bot
```
2. Run the Docker container:
```
docker run -it --name printer-bot printer-bot
```
3. Find the bot on Telegram by searching for "@your_bot_username"
4. Send any document to the bot and it will be sent to the printer.

## Note

- Make sure the printer is connected and turned on before running the bot.
- Only one printer can be connected to the bot at a time.
- The bot is only able to print files that are sent to it in a Telegram chat.
- Additional configuration may be necessary if the printer requires specific settings or drivers.


https://python-forum.io/Thread-cups-printing

should be running on a CUPS server
make use of following command
`lp filename` uses default server printer to print

I'm not sure how to containerize it

- lp command must be missing
- do I have to forward USB devices ?
