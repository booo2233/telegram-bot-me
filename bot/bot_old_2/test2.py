"""
from telegram import Update
from telegram.ext import *
BOT = "6484814773:AAGj0V1or3ihz_6jSSFi0OUJjTlp608_AJc"
async def hanld(update:Update, context:ContextTypes.DEFAULT_TYPE):

    file = await context.bot.get_file(update.message.photo[-1].file_id)
    await file.download_to_drive()
    await update.message.reply_text("all_good")


if __name__ == "__main__":
    print("starting") 
    app = ApplicationBuilder().token(BOT).build()
    app.add_handler(MessageHandler(filters.PHOTO, hanld))
    print("starting polling")
    app.run_polling(0)
"""
import os

os.chdir("test_ai")

with open("system.txt", "r",encoding="utf-8") as f:
    text = f.read()
    print(text)

print(text)