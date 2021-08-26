import click


@click.group()
def main():
    pass


@main.command()
@click.option('-username', prompt='Enter your username: ', help='To put your username')
@click.option('-message', prompt='Enter your message: ', help='To put your message')
def init(username, message):
    write = str(input('Do you want to create a new text file and save it on your system? [Y/n]: '))
    save_user_message = [username, message]
    result = ('Username: ' + save_user_message[0],
              'User Message: ' + save_user_message[1])
    if write == 'Y' or write == 'y':
        file_txt = open("Visit_Book", "w")
        file_txt.writelines(result)
        click.echo('File created! Check your File Manager!')
    else:
        print('Username: ' + save_user_message[0],
              'User Message: ' + save_user_message[1])

    click.echo('Check my GitHub and my projects!')
    click.echo('https://github.com/victorhenrique07/Code-Generator')
    click.echo('https://github.com/victorhenrique07/Web-Crawler')


@main.command()
def cg():
    click.echo('This repository is a project that will generate a random code'
               ' of 8 characters of A until Z and 0 until 9..')
    click.echo('It is made in only Python')
    click.echo('Go test it! https://github.com/victorhenrique07/Code-Generator')


@main.command()
def wb():
    click.echo('This repository is Web Crawler. It gonna login into your instagram and like some random pics.')
    click.echo('It is made in only Python too!')
    click.echo('https://github.com/victorhenrique07/Web-Crawler')


if __name__ == "__main__":
    main()
