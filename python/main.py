from flask import Flask, request, jsonify, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import app.py


app = Flask(__name__)
app.secret_key = 'your_secret_key'

# In-memory data stores
users = {}
posts = []

# Helper functions
def current_user():
    username = session.get('username')
    if username and username in users:
        return username
    return None

# Routes

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'error': 'Username and password required'}), 400
    if username in users:
        return jsonify({'error': 'User already exists'}), 400
    users[username] = generate_password_hash(password)
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if username not in users or not check_password_hash(users[username], password):
        return jsonify({'error': 'Invalid credentials'}), 401
    session['username'] = username
    return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    return jsonify({'message': 'Logged out successfully'}), 200

@app.route('/post', methods=['POST'])
def create_post():
    user = current_user()
    if not user:
        return jsonify({'error': 'Authentication required'}), 401
    data = request.json
    content = data.get('content')
    if not content:
        return jsonify({'error': 'Content required'}), 400
    post = {
        'id': len(posts) + 1,
        'author': user,
        'content': content
    }
    posts.append(post)
    return jsonify({'message': 'Post created', 'post': post}), 201

@app.route('/feed', methods=['GET'])
def feed():
    return jsonify({'posts': posts[::-1]}), 200

if __name__ == '__main__':
    app.run(debug=True)