from message_board_v1.models import SelfUser, Message_v1

import bcrypt

def bad_create_user(username, password):
    new = SelfUser(username=username, password=password)
    new.save()

def bad_check_password(username, password):
    if found := SelfUser.objects.filter(username=username).first():
        if found.password == password:
            print(f"{username} logged in")
            return True
        
    return False


def better_create_user(username, password):
    # converting password to array of bytes
    encoded_password = password.encode('utf-8')
  
    # generating the salt
    salt = bcrypt.gensalt()
    
    # Hashing the password
    hashed = bcrypt.hashpw(encoded_password, salt)

    new = SelfUser(username=username, password=hashed)
    new.save()


def better_check_password(username, password):
    encoded_password = password.encode('utf-8')

    if found := SelfUser.objects.filter(username=username).first():
        return bcrypt.checkpw(encoded_password, found.password)  
             
    return False
   

def bad_filter_messages(message):
    query = f'%%{message}%%'
    filtered = Message_v1.objects.raw("SELECT * FROM message_board_v1_message_v1 WHERE content LIKE '" + query + "'")

    # Fixed the SQL Injection problem by using parameters instead
    #filtered = Message_v1.objects.raw("SELECT * FROM message_board_v1_message_v1 WHERE content LIKE %s", [query])

    result = []
    for row in filtered:
        result.append({"content": row.content, "user__username": row.user.username})
    return result