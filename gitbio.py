import requests
from colored import fg, attr, stylize

API_URL = 'https://api.github.com/users'

def introAndAsk():
    print('')
    print("%sWelcome to your GitHub Bio Viewer CLI, that shows your bio in Terminal. If you want to exit, press q and enter on question input to quit program. %s" % (fg(4), attr(0)))
    ask = input("%sWhat's Your Name On GitHub?:%s " % (fg(2), attr(0)))
    print('')

    stylize(ask, fg(1))

    if ask == "q":
        exit()

    return ask

while True:
    # Get My Profile From GitHub API
    response = requests.get(f'{API_URL}/{introAndAsk()}?bio')

    # Parse JSON
    user_name = response.json()

    # Get Username
    bio = user_name["bio"]    

    # Show text
    print(f'%s{bio} %s' % (fg(1), attr(0)))