import json
import random
import time
import sys

def update_leaderboard(username, wpm):
    leaderboard_file = "leaderboard.json"

    try:
        with open(leaderboard_file, "r") as file:
            leaderboard = json.load(file)
    except FileNotFoundError:
        leaderboard = []
        
    leaderboard.append({"username": username, "wpm": wpm})
    leaderboard.sort(key=lambda x: x["wpm"], reverse=True)

    with open(leaderboard_file, "w") as file:
        json.dump(leaderboard[:10], file)

def show_leaderboard():
    leaderboard_file = "leaderboard.json"

    try:
        with open(leaderboard_file, "r") as file:
            leaderboard = json.load(file)
        print("\n=== Leaderboard ===")
        for i, entry in enumerate(leaderboard, start=1):
            print(f"{i}. {entry['username']}: {entry['wpm']} WPM")
    except FileNotFoundError:
        print("Leaderboard is empty.")