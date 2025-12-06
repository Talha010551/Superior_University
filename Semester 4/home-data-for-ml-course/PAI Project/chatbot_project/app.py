from flask import Flask, render_template, request, jsonify
import json
import os
from utils import get_response, load_intents

app = Flask(__name__)

# Load intents using utility (returns list of intents)
intents = load_intents('intents.json')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    if not user_message:
        return jsonify({'response': 'Please enter a message.'})
    
    response = get_response(user_message, intents)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
