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






# Recording the steps that I followed on a new raspberry pi 3 to make a non network printer available on network 
objective was to make printing and scanning available on network

printer: HP deskjet 2300 All in one
## for printer
 - install hplip from debain repo `sudo apt-get install hplip`
 - install cups `sudo apt-get install cups`
 - add printer to cups from web, and share the printer to allow print from internet
 - printer should be available on local network to print
## for scanner
 - install sane and configure it
   - follow this guide https://github.com/sbs20/scanservjs/blob/master/docs/sane.md
   - install sane
   - add user to group scanner
   - make sure scanner is detected by `scanimage -L`
 - install docker (part of above guide)
 - start scansrvjs docker container
 - set static IP for pi in router
 - (optional) install cloudflared to expose it to internet 
