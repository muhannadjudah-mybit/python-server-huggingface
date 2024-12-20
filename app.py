from flask import Flask, request, jsonify
from dotenv import load_dotenv
import requests
import os
# Load .env file
load_dotenv()

app = Flask(__name__)

# Your Hugging Face API token

API_TOKEN = os.getenv('HUGGING_FACE_API_TOKEN')

API_URL = "https://api-inference.huggingface.co/models/gpt2"
#  gpt2
#  openai-community/gpt2
#  google/gemma-2-2b-it


# A function to send requests to Hugging Face API
def generate_text(input_text):
    headers = {
        'Authorization': f'Bearer {API_TOKEN}',
        'Content-Type': 'application/json',
    }

    payload = {
        'inputs': input_text
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    # Check if the response is successful
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Something went wrong with the API request."}

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    input_text = data.get('text', '')
    
    if input_text:
        result = generate_text(input_text)
        return jsonify(result)
    else:
        return jsonify({"error": "No input text provided"}), 400

if __name__ == '__main__':
    app.run(debug=True)