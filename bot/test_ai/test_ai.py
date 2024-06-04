
from PIL import Image
from dotenv import load_dotenv
import os
import google.generativeai as genai
from settings import *
import asyncio

text_sys : str = ""
load_dotenv()
key = os.getenv("GEMINI_API_KEY")

image_name : str = ""
print(image_name)

os.chdir("test_ai")
with open("system.txt", "r", encoding="utf-8") as f:
 text_sys = f.read()
os.chdir("..")

async def handle_response(text: str,) -> str:
#key
  genai.configure(api_key=key)
#settings
  generation_config : dict = generation_configes
  safety_settings : list = safety_settingses
#main sand api call


  model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    safety_settings=safety_settings,
    generation_config=generation_config,
    system_instruction=text_sys
  )
  chat_session = model.start_chat(
    history=[
    ]
  )
  text = text.lower()
  

  
  response = chat_session.send_message([text], stream=True)
  response.resolve()
  return response.text

       

