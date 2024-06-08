"""
import google.generativeai as genai
import os
import time
from settings import *
import asyncio

print("lol")
key = "AIzaSyDhpGqvdZVhWE73HW_z_CKCcbYMVa6SAqo"
genai.configure(api_key=key)

def upload_to_gemini(path, mime_type=None):
  
  file = genai.upload_file(path, mime_type=mime_type)
  print(f"Uploaded file '{file.display_name}' as: {file.uri}")
  print("lol")
  return file
  
  
print("lol")


files = [
upload_to_gemini("r.mp3", mime_type="audio/mp3"),
 ]
print("lol")
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    safety_settings=safety_settingses,
    generation_config=generation_configes,
    system_instruction="be good ai your name = gemini"
                              )
print("lol")
# Make the LLM request.
print("Making LLM inference request...")
print(files)
response = model.generate_content([files[0]])
print(response.text)
print("lol")
"""

text = "https://www.wyoube.com"
text = text.replace("www." ,"")
print(text)
