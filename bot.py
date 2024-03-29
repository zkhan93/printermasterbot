import os
import time
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger("bot")

token = os.getenv("TOKEN")
allowed_usernames = os.getenv("ALLOWED_USERNAMES", "").split()
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I'm Printer, send me a photo or document to print!",
    )


def clean(update, context):
    if os.path.exists("data"):
        os.system("rm -f ./data/*")
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Cleaning up old downloaded files from data folder",
    )


def print_msg(update, context):
    logger.info(type(update))
    logger.info(update.effective_message)
    file = None
    if update.effective_message.photo:
        photo = max(update.effective_message.photo, key=lambda x: x.file_size)
        file = photo.get_file()
    if update.effective_message.document:
        file = update.effective_message.document.get_file()
    if not os.path.exists("data"):
        os.mkdir("data")
    file_path = file.download(os.path.join("data", str(int(time.time()))), timeout=100)
    logger.info(f"file saved at {file_path}")
    print_file(file_path)
    context.bot.send_message(chat_id=update.effective_chat.id, text="printing...")


def print_file(file):
    logger.info(f"printing {file}")
    logger.debug(f"/usr/bin/lp -o fit-to-page -o media=A4 {file}")
    logger.info(os.system(f"/usr/bin/lp -o fit-to-page -o media=A4 {file}"))


start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)

clean_handler = CommandHandler(
    "clean", clean, filters=Filters.chat(username=allowed_usernames)
)
dispatcher.add_handler(clean_handler)

print_handler = MessageHandler(
    Filters.chat(username=allowed_usernames)
    & (Filters.photo | Filters.document)
    & (~Filters.command),
    print_msg,
)
dispatcher.add_handler(print_handler)

updater.start_polling()
