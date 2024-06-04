from telegram import Update
from telegram.ext import *
from dotenv import load_dotenv
import os
from gemini.text_response import *
from gemini.image_response import *
from gemini.video_response import *
load_dotenv()

TELEGRAM_API_KEY : str = os.getenv("BOT_TELE_KEY")
TELEGRAM_BOT_NAME : str = "@ai_gemini_bot"

#Commands for the bot
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Thanks for chatting with! me! I am a cat")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("l am a cat! pls type something so l can respond")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command!")



async def telegram_bot(update : Update, context : ContextTypes.DEFAULT_TYPE):
     # message_type Get group type public, private or group chat Second line looks for new text messages in chat
     message_type: str = update.message.chat.type
     text : str = update.message.text
     print(f"User ({update.message.chat.id}) in {message_type}: {text}")

     if update.message.text:
              message_type: str = update.message.chat.type
              text : str = update.message.text

             # cheque if it is group or  private chat

              if message_type == "group":
                 if TELEGRAM_BOT_NAME in text:
                      new_text: str = text.replace(TELEGRAM_BOT_NAME, "").split()
                      response: str = await handle_response(text, f"{update.message.chat.id}.jpg")
                 else:
                     return
             
             #not group send message
              else:
                   response: str = handle_response(text)
              #send message and print(response)
              print(f"bot: {response}")
              await update.message.reply_text(response, parse_mode="Markdown")
     elif update.message.photo:
            #Get the image ID
            file = await context.bot.get_file(update.message.photo[-1].file_id)
            file_name = f"{update.message.chat.id}.jpg"
            download_folder = "image"
            #get caption of image

            caption = update.message.caption
            #Download the image
            if caption == None:
                 await update.message.reply_text("No captin")
            await file.download_to_drive(custom_path=os.path.join(download_folder, file_name))
            image_name = f"{update.message.chat.id}.jpg"
            
            #Send confirmation
            await update.message.reply_text(f"photo downloaded Successfully we are currently processing your image After proofing the image will be deleted {image_name}" , parse_mode="Markdown")
            print(f"{image_name}")

            response_of_image = await image_response(caption, image_name)
            
            await update.message.reply_text(response_of_image, parse_mode="Markdown")
     elif update.message.video:

              chat_id = update.message.chat.id
              download_folder_video = "video"
              file_name = update.message.video.file_name
              file = await context.bot.get_file(update.message.video.file_id)
              caption_video = update.message.caption

              if file_name != None:
                               file_name_ex = update.message.video.file_name.split(".")[-1]
                               video_name = f"{chat_id}.{file_name_ex}"

                               
                               await file.download_to_drive(custom_path=os.path.join(download_folder_video, video_name))
              else:
                               video_name = f"{chat_id}.mp4"
                               await file.download_to_drive(custom_path=os.path.join(download_folder_video, video_name)) 
                   
              if caption_video == None:
                     await update.message.reply_text("no captino")
              
              else:
                     response_of_video = video_response(caption_video, video_name)

                     await update.message.reply_text(response_of_video)
               



     else:
          await update.message.reply_text("**oops**", parse_mode="Markdown")

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
     print(f"Update {update} casued error {context.error}")

if __name__ == "__main__":
    print("strarting....")
    app = ApplicationBuilder().token(TELEGRAM_API_KEY).build()
     
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))

    app.add_handler(MessageHandler(filters.ALL, telegram_bot))
    
    app.add_error_handler(error)
    print("polling...")
    app.run_polling(poll_interval=0)    