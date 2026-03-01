from flask import Flask, request, jsonify, render_template
from googletrans import Translator
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
translator = Translator()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():
    user_input = request.json["text"]
    translated = translator.translate(user_input, dest="en")
    english_prompt = translated.text
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": english_prompt}]
    )
    ai_response = response.choices[0].message.content
    return jsonify({"translated": english_prompt, "response": ai_response})

if __name__ == "__main__":
    app.run(debug=True)
