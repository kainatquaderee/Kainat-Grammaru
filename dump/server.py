from flask import Flask, request, jsonify
from flask_cors import CORS
from flask import Flask, request, jsonify
import streamlit as st
from hugchat import hugchat
from hugchat.login import Login
from dotenv import load_dotenv
import os


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def process_text(input_text,email, passwd):
    # Hugging Face Login
    sign= Login(email,passwd)
    cookie= sign.login()
    #create chatbot
    chatbot= hugchat.ChatBot(cookies=cookies.get_dict())
    chatbot.new_conversation(assistant="67e23a545deaaed36e03ca47", switch_to=True)
    message_result = chatbot.chat(input_text)
    return message_result  # Modify this logic as needed

@app.route('/process', methods=['POST'])
def process():
    data = request.json

    load_dotenv()

    email="kainatquaderee@gmail.com"
    passwd="KainatOgaTQBG2000"
    modified_text = process_text(data.get("text", ""),email,passwd)
    print("Modified text:", modified_text)  # Debugging output
    return jsonify({"modified_text": modified_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
