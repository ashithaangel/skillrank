# app.py
from flask import Flask, jsonify, request
import json

app = Flask('app')

# Load user data from users.json
with open('users.json', 'r') as file:
    users = json.load(file)

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Check if username exists and password matches
    for user in users:
        if user['username'] == username and user['password'] == password:
            return jsonify({"message": "Login successful"})
    
    # If no matching user found
    return jsonify({"error": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(debug=True)
