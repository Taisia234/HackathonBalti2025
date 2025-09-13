# app.py
from flask import Flask, request, jsonify
from users import register_user, authenticate_user
from posts import create_post, view_posts, update_post, delete_post
from auth import is_authorized

app = Flask(__name__)

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    success = register_user(data["email"], data["password"])
    if success:
        return jsonify({"message": "✅ Registered successfully"})
    return jsonify({"error": "User already exists"}), 400

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    if authenticate_user(data["email"], data["password"]):
        return jsonify({"message": "✅ Login successful"})
    return jsonify({"error": "Invalid credentials"}), 401

@app.route("/create", methods=["POST"])
def create():
    email = request.headers.get("X-User-Email")
    post_id = request.json.get("post_id")
    content = request.json.get("content")
    ok, _ = is_authorized(email, "create", post_id)
    if ok:
        post = create_post(post_id, content)
        return jsonify(post)
    return jsonify({"error": "❌ Unauthorized"}), 403

@app.route("/view", methods=["GET"])
def view():
    email = request.headers.get("X-User-Email")
    ok, _ = is_authorized(email, "view")
    if ok:
        return jsonify(view_posts())
    return jsonify({"error": "❌ Unauthorized"}), 403

@app.route("/update", methods=["PUT"])
def update():
    email = request.headers.get("X-User-Email")
    post_id = request.json.get("post_id")
    content = request.json.get("content")
    ok, _ = is_authorized(email, "update", post_id)
    if ok:
        post = update_post(post_id, content)
        if post:
            return jsonify(post)
        return jsonify({"error": "Post not found"}), 404
    return jsonify({"error": "❌ Unauthorized"}), 403

@app.route("/delete", methods=["DELETE"])
def delete():
    email = request.headers.get("X-User-Email")
    post_id = request.json.get("post_id")
    ok, _ = is_authorized(email, "delete", post_id)
    if ok:
        post = delete_post(post_id)
        if post:
            return jsonify({"message": "✅ Post deleted"})
        return jsonify({"error": "Post not found"}), 404
    return jsonify({"error": "❌ Unauthorized"}), 403

if __name__ == "__main__":
    app.run(debug=True)
