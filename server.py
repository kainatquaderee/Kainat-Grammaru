from flask import Flask, request, jsonify
from flask_cors import CORS
from hugchat import hugchat
from hugchat.login import Login
from dotenv import load_dotenv, dotenv_values
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load environment variables
# Automatically loads variables from `.env` file
load_dotenv()

hf_email = os.getenv("EMAIL")
hf_passwd = os.getenv("PASS")

def process_text(input_text, email, passwd):
    # Hugging Face Login
    sign = Login(email, passwd)
    cookies = sign.login()

    # Create chatbot
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    chatbot.new_conversation(assistant="67e23a545deaaed36e03ca47", switch_to=True)

    # Get the response from the chatbot
    message_result = chatbot.chat(input_text)

    # Assuming the message result is a dictionary with a 'text' key
    if isinstance(message_result, dict) and 'text' in message_result:
        return message_result['text']

    # If not, just return the message_result directly (or handle it as needed)
    return str(message_result)  # Convert any non-serializable object to string

@app.route('/process', methods=['POST'])
def process():
    data = request.json

    # Get input text and process it
    input_text = data.get("text", "")
    modified_text = process_text(input_text, hf_email, hf_passwd)

    print("Modified text:", modified_text)  # Debugging output

    # Return the modified text as a JSON response
    return jsonify({"modified_text": modified_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
