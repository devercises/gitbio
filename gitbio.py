import requests

API_URL = 'https://api.github.com/users'

def main():
    while True:
        # Get My Profile From GitHub API
        response = requests.get(f'{API_URL}/{introAndAsk()}?bio')

        # Parse JSON
        user_name = response.json()

        # Get Username
        bio = user_name["bio"]

        # Show text
        print(bio)

def introAndAsk():
    print("Welcome to your GitHub Bio Viewer CLI, that shows your bio in Terminal. If you want to exit, press Ctrl + C (Command + C on Mac) to quit program.")
    ask = input("What's Your Name On GitHub?: ")

    return ask