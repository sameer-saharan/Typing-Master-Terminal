import json
import random
import time
import sys

def load_words_from_json(category):
    words_data_file = "words_data.json"

    try:
        with open(words_data_file, "r") as file:
            words_data = json.load(file)

        if category in words_data:
            return words_data[category]
        else:
            print(f"Words for '{category}' not found in words_data.json.")
            return []
    except FileNotFoundError:
        print(f"Words data file '{words_data_file}' not found.")
        return []

def get_user_input():
    try:
        user_input = input(" << (Type the word exactly as shown.)\n")
    except KeyboardInterrupt:
        sys.exit("\n\nExiting the game. Goodbye!")

    return user_input