from telegram import Update
from telegram.ext import *

# Replace with your bot token
BOT = "6484814773:AAGj0V1or3ihz_6jSSFi0OUJjTlp608_AJc"


        # Get the highest resolution image
async def hanld(update: Update, context:ContextTypes.DEFAULT_TYPE):

           file = update.message.photo[-1]
           file_extension = file.file_name.split(".")[-1].lower()
           await update.message.reply_text(f"all_good {file_extension}")

if __name__ == "__main__":
    print("starting") 
    app = ApplicationBuilder().token(BOT).build()
    app.add_handler(MessageHandler(filters.PHOTO, hanld))
    print("starting polling")
    app.run_polling(0)


