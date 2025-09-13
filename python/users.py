# users.py
USERS = {
    "ivan.smith@gmail.com": {"password": "pass123", "role": "platform-moderator", "isSuperUser": True},
    "jane.doe@gmail.com": {"password": "pass456", "role": "platform-viewer", "isSuperUser": False},
    "admin@example.com": {"password": "adminpass", "role": "platform-admin", "isSuperUser": True},
}

def register_user(email, password, role="platform-user", isSuperUser=False):
    if email in USERS:
        return False
    USERS[email] = {"password": password, "role": role, "isSuperUser": isSuperUser}
    return True

def authenticate_user(email, password):
    user = USERS.get(email)
    return user and user["password"] == password
