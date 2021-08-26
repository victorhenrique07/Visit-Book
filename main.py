import click


@click.group()
def main():
    pass


@main.command()
@click.option('-username', prompt='Enter your username: ', help='To put your username')
@click.option('-message', prompt='Enter your message: ', help='To put your message')
@click.option('-write', prompt='Do you want to create a new text file and save it on your system? [Y/n]: ')
def init(username, message, write):
    save_user_message = [username, message]
    result = ('Username: ' + save_user_message[0],
              'User Message: ' + save_user_message[1])
    print('Username: ' + save_user_message[0],
          'User Message: ' + save_user_message[1])

    if write == 'Y' or 'y':
        file_txt = open("Visit_Book", "w")
        file_txt.writelines(result)


'''
Check my GitHub and my projects!
https://github.com/victorhenrique07/Code-Generator
https://github.com/victorhenrique07/Web-Crawler
'''


if __name__ == "__main__":
    main()
