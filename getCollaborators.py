import sys
import requests

if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) < 2:
        print("Usage: python getCollaborators.py <username> <password>")
        sys.exit(1)

    token = args[0]
    repo_name = args[1]

    data = requests.get(f"https://api.github.com/repos/{repo_name}/collaborators", headers={
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28"
    })

    print(data.json())