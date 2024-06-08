import asyncio
import os
from dotenv import load_dotenv
import google.generativeai as genai
from settings import *
load_dotenv()
GEMINI_KEY : str = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_KEY)

os.chdir("test_ai")
with open("system.txt", "r", encoding="utf-8") as f:
 text_sys = f.read()
os.chdir("..")

async def voice(file_voice_file_name:str) -> str:
 def upload_to_gemini(path, mime_type=None):

  file = genai.upload_file(path, mime_type=mime_type)
  print(f"Uploaded file '{file.display_name}' as: {file.uri}")
  return file


 model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  safety_settings=safety_settingses,
  generation_config=generation_configes,
  system_instruction=text_sys
 )

 os.chdir("audio")
 files = [
  upload_to_gemini(file_voice_file_name, mime_type="audio/ogg"),
 ]

 os.remove(file_voice_file_name)
 os.chdir("..")
 chat_session = model.start_chat(
   history=[
   ]
 )

 response = chat_session.send_message([files[0]], stream=True)
 response.resolve()
 return response.text
