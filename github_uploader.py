"""
GitHub Automatic Uploader for Ragshanth/POAI
Uses standard library (urllib) to upload all files to GitHub repository via GitHub REST API.

Usage:
  python github_uploader.py <YOUR_GITHUB_PERSONAL_ACCESS_TOKEN>
"""

import os
import sys
import json
import base64
import urllib.request
import urllib.error

REPO_OWNER = "Ragshanth"
REPO_NAME = "POAI"
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

# Files to exclude from upload
EXCLUDE = {"github_uploader.py"}

def get_file_sha(file_path, token):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{file_path}"
    req = urllib.request.Request(url, headers={
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "Antigravity-Uploader"
    })
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data.get("sha")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise

def upload_file(file_name, token):
    full_path = os.path.join(DIRECTORY, file_name)
    with open(full_path, "rb") as f:
        content_b64 = base64.b64encode(f.read()).decode("utf-8")

    sha = get_file_sha(file_name, token)
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{file_name}"
    
    payload = {
        "message": f"Upload {file_name}",
        "content": content_b64
    }
    if sha:
        payload["sha"] = sha

    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json",
            "Content-Type": "application/json",
            "User-Agent": "Antigravity-Uploader"
        },
        method="PUT"
    )

    try:
        with urllib.request.urlopen(req) as resp:
            if resp.status in (200, 201):
                print(f"[OK] Successfully uploaded: {file_name}")
                return True
    except urllib.error.HTTPError as e:
        print(f"[ERROR] Failed to upload {file_name}: {e.code} {e.reason}")
        return False

def main():
    token = sys.argv[1] if len(sys.argv) > 1 else os.getenv("GITHUB_TOKEN")
    if not token:
        print("Usage: python github_uploader.py <GITHUB_PERSONAL_ACCESS_TOKEN>")
        print("Or set the GITHUB_TOKEN environment variable.")
        return

    files = [f for f in os.listdir(DIRECTORY) if os.path.isfile(os.path.join(DIRECTORY, f)) and f not in EXCLUDE]
    print(f"Uploading {len(files)} files to https://github.com/{REPO_OWNER}/{REPO_NAME} ...")
    
    success = 0
    for f in sorted(files):
        if upload_file(f, token):
            success += 1

    print(f"\nDone! {success}/{len(files)} files uploaded successfully.")

if __name__ == "__main__":
    main()
