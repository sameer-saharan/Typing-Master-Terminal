import json
import random
import time
import sys
from leaderboard import update_leaderboard
from leaderboard import show_leaderboard
from typingmaster import load_words_from_json
from typingmaster import get_user_input

def main():
    print("Welcome to Terminal Typing Master!")

    username = input("Enter your username: ")
    
    while True:
        print("\nOptions:")
        print("1. Start Typing Test")
        print("2. Show Leaderboard")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            category = input("Choose a category (e.g., animals, fruits, country, city, cars): ")
            words = load_words_from_json(category)

            if not words:
                print("Invalid category or empty word list. Please try again.")
                continue

            input("Press Enter to start the typing test...")
            start_time = time.time()

            correct_words = 0
            for word in words:
                print(word, end=" ")
                user_input = get_user_input()
                if user_input.strip() == word:
                    correct_words += 1

            end_time = time.time()
            time_taken = round(end_time - start_time, 2)
            words_typed = len(words)
            wpm = int((words_typed / time_taken) * 60)

            print(f"\nTyping Test Complete!\nWords Typed: {correct_words}/{words_typed}\nTime Taken: {time_taken} seconds\nWords Per Minute: {wpm} WPM")

            update_leaderboard(username, wpm)

        elif choice == "2":
            show_leaderboard()

        elif choice == "3":
            print("Exiting the Game. Goodbye!")
            sys.exit()

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
