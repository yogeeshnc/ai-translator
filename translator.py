from googletrans import Translator
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

translator = Translator()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

user_input = input("Enter your prompt in any language: ")

translated = translator.translate(user_input, dest='en')
english_prompt = translated.text
print("Translated to English:", english_prompt)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": english_prompt}]
)

print("AI Response:", response.choices[0].message.content)