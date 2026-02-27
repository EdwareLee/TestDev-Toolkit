import requests

def get_github_user(username: str) -> dict:
    resp = requests.get(f"https://api.github.com/users/{username}")
    resp.raise_for_status()
    return resp.json()