import requests

# services gets json from the github api
def get_repos():
    url = 'https://api.github.com/users/cojoe123/repos'
    response = requests.get(url)
    info = response.json()
    return info
