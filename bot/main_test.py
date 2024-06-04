import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
from test_ai.test_ai import *
import asyncio
from test_ai.video_ai import video_ai
from test_ai.audio_ai import audio

load_dotenv()

BOT_TOKEN : str = os.getenv("BOT_TELE_KEY")
BOT_USERNAME : str = "@ai_gemini_bot"

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Thanks for chatting with! me! I am a cat")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("l am a cat! pls type something so l can respond")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command!")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
   
    video = update.message.video
    if update.message.photo:
            file = await context.bot.get_file(update.message.photo[-1].file_id)
            os.chdir("image")
            await file.download_to_drive(f"{update.message.chat.id}.jpg")
            image_name = f"{update.message.chat.id}.jpg"
            os.chdir("..")
            await update.message.reply_text("image Done ready to ask questions tell me AI to use the image. use img or IMG like img what in the image" , parse_mode="Markdown")
            print(f"{image_name} main")



    elif update.message.video:
        
               
        ################des########################
               chat_id = update.effective_chat.id
               #file_extension = video.file_name.split('.')[-1]  # Extract the extension

        # Get file information
               new_file =  await context.bot.get_file(update.message.video.file_id)

        # Download the video to the 'downloads' folder, using chat ID as file name
               download_folder = 'video'
               os.makedirs(download_folder, exist_ok=True)

               file_name = f"{chat_id}.mp4"

               await new_file.download_to_drive(custom_path=os.path.join(download_folder, file_name))
               caption =  update.message.caption

               await context.bot.send_message(
                 chat_id=chat_id, 
                 text=f"Video downloaded successfully as: *{file_name}* Unlike images, which processed videos get immediately deleted after processing",
                 parse_mode='Markdown'
                )
               if caption == None:
                await update.message.reply_text("No caption add a caption" ,parse_mode="Markdown")
               else:
                await update.message.reply_text(f"{context.error}")
                response_video =  video_ai(caption, file_name)
                await update.message.reply_text(response_video, parse_mode="Markdown")

    else:
     message_type: str = update.message.chat.type
     text : str = update.message.text
     CHAT_ID_IMG = f"{update.message.chat.id}.jpg"
     print(f"User ({update.message.chat.id}) in {message_type}: {text}")

     if message_type == "group":
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, "").split()
            response: str = await handle_response(text, f"{update.message.chat.id}.jpg")
        else:
            return
     else:
        response: str = await handle_response(text, f"{update.message.chat.id}.jpg")
    
    print("bot", response)
    await update.message.reply_text(response, parse_mode="Markdown")

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} casued error {context.error}")
    



if __name__ == "__main__":

    print("strarting....")
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))

    app.add_handler(MessageHandler(filters.ALL, handle_message))
    
    app.add_error_handler(error)
    print("polling...")
    app.run_polling(poll_interval=0)

