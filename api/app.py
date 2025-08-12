#IMPORTS
import google.generativeai as genai
from dotenv import load_dotenv
from flask import Flask, request, jsonify,send_from_directory
import os

#LOADING ENVIRONMENT VARIABLES
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

#CONFIGURING GOOGLE GENERATIVE AI
genai.configure(api_key=GOOGLE_API_KEY)
model=genai.GenerativeModel("gemini-1.5-flash")

#FLASK APP SETUP
app = Flask(__name__)

#BASIC ROUTE
@app.route("/")
def home():
    return send_from_directory("static", "index.html")

#CHAT ROUTE
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    msg = data.get("message", "")

    if not msg:
        return jsonify({"ladybug": "Please enter a message"}), 400

    try:
        response = model.generate_content(msg)

        return jsonify({"ladybug": response.text})
    except Exception as e:
        return jsonify({"ladybug": f"Error: {str(e)}"}), 500

