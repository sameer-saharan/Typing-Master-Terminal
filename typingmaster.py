import json
import random
import time
import sys

def load_words_from_json(category):
    words_file = f"{category.lower()}_words.json"

    try:
        with open(words_file, "r") as file:
            words_data = json.load(file)
        return words_data["words"]
    except FileNotFoundError:
        print(f"Words file for '{category}' not found.")
        return []

def get_user_input():
    try:
        user_input = input(" << Type the word exactly as shown.\n")
    except KeyboardInterrupt:
        sys.exit("\n\nExiting the game. Goodbye!")

    return user_input