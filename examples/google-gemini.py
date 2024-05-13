import google.generativeai as genai
import os

print("Thanks for reaching out to sanjeev from Heal @ Home")
print("Our goal is to make it easier for you to schedule Telemedicine appointments")
print("This is NOT medical advise.")

print("*****************************")
print("Please set your api key in the GOOGLE_API_KEY env variable to test.")
print("*****************************")

genai.configure(api_key="") # Add API key here

model = genai.GenerativeModel('gemini-1.0-pro-latest')

while True:
    val = input("You: ")
    response = model.generate_content(val)
    print(f'Bot: {response.text}')

