import random

# 🎯 Themes and their word lists
themes = {
    "marvel": ["ironman", "spiderman", "thanos", "loki", "wanda", "vision", "deadpool", "thor", "captainamerica", "dr doom"],
    "names": ["utkarsh", "preeti", "harshit", "shlok", "akshay", "vaishnavi", "arjun", "charu", "saurya", "shipra"],
    "cars": ["toyota", "honda", "bmw", "audi", "ford", "tesla", "mercedes", "hyundai", "lamborgini", "ferrari"],
    "countries": ["india", "brazil", "canada", "germany", "australia", "china", "france", "usa", "russia"],
    "cricketers": ["kohli", "dhoni", "rohit", "warner", "shreyas", "hardik", "jadeja", "gayle"]
}

def choose_word(theme):
    return random.choice(themes[theme])

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def select_theme():
    print("🎮 Choose a theme:")
    for i, theme in enumerate(themes.keys(), 1):
        print(f"{i}. {theme.capitalize()}")

    while True:
        choice = input("Enter the number of your choice: ")
        if choice.isdigit() and 1 <= int(choice) <= len(themes):
            return list(themes.keys())[int(choice) - 1]
        else:
            print("❌ Invalid choice. Please try again.")

def hangman():
    print("🧩 Welcome to Themed Hangman!")
    theme = select_theme()
    word = choose_word(theme)
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = 5

    print(f"\n🎯 Theme: {theme.capitalize()}")
    print(f"You have {max_wrong} wrong attempts. Let's go!\n")

    while wrong_guesses < max_wrong:
        print(display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("🔁 You've already guessed that.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("✅ Good guess!\n")
            if all(letter in guessed_letters for letter in word):
                print(f"🎉 You won! The word was: {word}")
                break
        else:
            wrong_guesses += 1
            print(f"❌ Wrong! Remaining attempts: {max_wrong - wrong_guesses}\n")

    else:
        print(f"💀 You lost! The word was: {word}")

# Start the game
if __name__ == "__main__":
    hangman()
