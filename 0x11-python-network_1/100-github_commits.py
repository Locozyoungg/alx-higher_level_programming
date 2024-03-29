#!/usr/bin/python3
"""
Lists 10 commits (from the most recent to oldest) of a repository by a user.
"""

import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()[:10]  # Get the most recent 10 commits
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print("Error:", response.status_code)
