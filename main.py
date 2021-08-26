username = str(input('Enter your username: '))
message = str(input('Enter your message here: '))


def user_message():
    save_user_message = [username, message]
    print('Username: ' + save_user_message[0],
          'User Message: ' + save_user_message[1])


user_message()
