

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# Enable logging for debugging (optional but recommended)

# Replace with your bot's token
BOT_TOKEN = "6484814773:AAGj0V1or3ihz_6jSSFi0OUJjTlp608_AJc"

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):

    photo_file = await context.bot.get_file(update.message.photo[-1].file_id)

    await photo_file.download_to_drive('received_photo.jpg') 

    await update.message.reply_text("Image received and downloaded!")
if __name__ == '__main__':
    print("str__name")
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Add the handler for photo messages
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    print("Start the bot")
    application.run_polling(0) 

"""from telegram.ext import Updater, MessageHandler, Filters

BOT_TOKEN = ' ... '

def downloader(update, context):
    context.bot.get_file(update.message.document).download()

    # writing to a custom file
    with open("custom/file.doc", 'wb') as f:
        context.bot.get_file(update.message.document).download(out=f)


updater = Updater(BOT_TOKEN, use_context=True)

updater.dispatcher.add_handler(MessageHandler(Filters.document, downloader))

updater.start_polling()
updater.idle()

Video:

message.video.file_id

Audio:

message.audio.file_id

Photo:

message.photo[2].file_id
"""