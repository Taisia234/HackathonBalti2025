# posts.py
POSTS = {}

def create_post(post_id, content):
    POSTS[post_id] = {"content": content}
    return POSTS[post_id]

def view_posts():
    return POSTS

def update_post(post_id, content):
    if post_id in POSTS:
        POSTS[post_id]["content"] = content
        return POSTS[post_id]
    return None

def delete_post(post_id):
    return POSTS.pop(post_id, None)
