import google.generativeai as genai
import os
import time
from settings import *
import asyncio

key = "AIzaSyDhpGqvdZVhWE73HW_z_CKCcbYMVa6SAqo"
genai.configure(api_key=key)

os.chdir("test_ai")
with open("system.txt", "r", encoding="utf-8") as f:
 text_sys = f.read()
os.chdir("..")

def audio(audio_file):
 def upload_to_gemini(path, mime_type=None):

   file = genai.upload_file(path, mime_type=mime_type)
   print(f"Uploaded file '{file.display_name}' as: {file.uri}")
   print("lol")
   return file
  

 os.chdir("audio")
 files = [
  upload_to_gemini(audio_file, mime_type="audio/mp3"),
  ]
 
 os.remove(audio_file)
 
 os.chdir("..")
 model = genai.GenerativeModel(
     model_name="gemini-1.5-pro",
     safety_settings=safety_settingses,
     generation_config=generation_configes,
     system_instruction=text_sys
                              )

# Make the LLM request.
 print("Making LLM inference request...")
 print(files)
 response = model.generate_content([files[0]])
 return response.text


