from dotenv import load_dotenv
import os
import google.generativeai as genai
from settings import *
import asyncio
from PIL import Image

load_dotenv()

GEMINI_API_KEY : str = os.getenv("GEMINI_API_KEY_IMAGE")

os.chdir("test_ai")
with open("system.txt", "r", encoding="utf-8") as f:
 text_sys = f.read()
os.chdir("..")


async def image_response(text:str, image_file_name:str) -> str:
  
  genai.configure(api_key=GEMINI_API_KEY)
  def upload_to_gemini(path, mime_type=None):

   file = genai.upload_file(path, mime_type=mime_type)
   print(f"Uploaded file '{file.display_name}' as: {file.uri}")
   return file
  
  os.chdir("image")

  files = [
  upload_to_gemini(image_file_name, mime_type="image/jpeg")]

  os.remove(image_file_name)
  os.chdir("..")
  
   
  text = text.lower()
  generation_config : dict = generation_configes
  safety_settings : list = safety_settingses

  model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    safety_settings=safety_settings,
    generation_config=generation_config,
    system_instruction=text_sys
  )
  chat_session = model.start_chat(
    history=[
    ]
  )
  
  response = chat_session.send_message([text, files[0]], stream=True)
  response.resolve()
  return response.text

          
 