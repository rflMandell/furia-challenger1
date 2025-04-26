online_users = set()

def add_user(username):
    online_users.add(username)

def remove_user(username):
    online_users.discard(username)
    
def get_online_users():
    return list(online_users)