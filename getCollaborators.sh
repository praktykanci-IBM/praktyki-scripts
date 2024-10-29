#!/bin/sh

if [ "$#" -lt 2 ]; then
    echo "Usage: getCollaborators.sh <token> <repo>"
    exit 1
fi

curl -L \
    -H "Accept: application/vnd.github+json" \
    -H "Authorization: Bearer $1" \
    -H "X-GitHub-Api-Version: 2022-11-28" \
    https://api.github.com/repos/$2/collaborators
