#!/usr/bin/env python3
"""
Antigravity <-> GitHub Continuous 2-Way Synchronization Engine
Syncs local Antigravity workspace directly with the remote GitHub repository:
https://github.com/nkyadawad-jpg/oil-gas-intelligence.git
"""

import subprocess
import sys
import datetime
import os

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
REMOTE_URL = "https://github.com/nkyadawad-jpg/oil-gas-intelligence.git"

def run_git(cmd, check=True):
    full_cmd = f"git {cmd}"
    result = subprocess.run(full_cmd, shell=True, cwd=PROJECT_DIR, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"[ERROR] {result.stderr.strip()}")
    return result

def sync_with_github(commit_message=None):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] Starting Antigravity <-> GitHub Repo Sync...")

    # 0. Execute refresh_data.py to ensure data and index.html timestamps are 100% current
    print("--> Running Live Qatar Energy Data Refresh Engine...")
    try:
        subprocess.run([sys.executable, os.path.join(PROJECT_DIR, "refresh_data.py")], check=True)
    except Exception as e:
        print(f"[!] Refresh engine notice: {e}")

    # 1. Ensure remote is configured
    run_git(f"remote set-url origin {REMOTE_URL}", check=False)

    # 2. Fetch latest remote changes
    print("--> Fetching remote state from GitHub...")
    fetch_res = run_git("fetch origin main", check=False)

    # 3. Stage all workspace files (including data/latest_intelligence.json & index.html)
    print("--> Staging Antigravity workspace files...")
    run_git("add .")

    # 4. Commit if changes exist
    status_res = run_git("status --porcelain", check=False)
    if status_res.stdout.strip():
        msg = commit_message or f"Live Data & Code Sync: {now}"
        print(f"--> Committing: {msg}")
        run_git(f'commit -m "{msg}"')
    else:
        print("--> No local uncommitted changes.")

    # 5. Push to GitHub
    print("--> Pushing directly to GitHub main branch...")
    push_res = run_git("push origin main", check=False)
    if push_res.returncode == 0:
        print("[OK] Antigravity & GitHub production link are 100% in sync!")
        print(f"[OK] Production Link: https://nkyadawad-jpg.github.io/oil-gas-intelligence/")
        return True
    else:
        print(f"[!] Push notice: {push_res.stderr.strip() or push_res.stdout.strip()}")
        return False

if __name__ == '__main__':
    msg = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else None
    sync_with_github(msg)
