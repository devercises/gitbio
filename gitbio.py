#!/usr/bin/env python

import requests
from colored import fg, attr

# GitHub API URL
API_URL = 'https://api.github.com/users'

# Function to show welcome message and read input from user
def introAndAsk():
    print('')

    # Say hello to user
    print("%sWelcome to your GitHub Bio Viewer CLI, that shows your bio in Terminal. If you want to exit, press q and enter on question input to quit program. %s" % (fg(4), attr(0)))
    
    # Ask for GitHub username
    ask = input("%sWhat's Your Name On GitHub?:%s " % (fg(2), attr(0)))
    
    print('')

    # Check if user wants to quit program, if true - exit
    if ask == "q":
        exit()

    # Return input
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