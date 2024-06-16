import csv
import random

def fetch_words(level):
    words = []
    with open('words.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        level_words = [row[f'Level {level}'] for row in reader]
        words = random.sample(level_words, 7)  # Choose 7 random words from the level
    return words

def scramble_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)

def ask_question(word):
    scrambled_word = scramble_word(word)
    user_answer = input(f"Unscramble the word: {scrambled_word}\nYour answer: ")

    if user_answer.lower() == word.lower():
        print("Correct!")
        return True
    else:
        print("Wrong!")
        return False

def main():
    print("Welcome to the Word Scramble Game!")

    username = input("Enter your username: ")
    score = 0

    for level in range(1, 4):  # Three levels in total
        print(f"\nLevel {level}")
        print("-------------")
        level_score = 0

        words = fetch_words(level)
        for word in words:  # Loop through words in the level
            if ask_question(word):
                level_score += 1

        print(f"\nLevel {level} over!")
        print(f"Score for Level {level}: {level_score}/7")
        score += level_score

        if level < 3:
            choice = input("Enter 'next' to go to the next level or 'exit' to quit: ")
            if choice.lower() != 'next':
                break

    print(f"\nGame Over, {username}!")
    print(f"Total Score: {score}/21")  # Total questions = 3 levels * 7 questions

if __name__ == "__main__":
    main()

# output:
# Welcome to the Word Scramble Game!
# Enter your username: rahul

# Level 1
# -------------
# Unscramble the word: tree
# Your answer: tree
# Correct!
# Unscramble the word: drao
# Your answer: road
# Correct!
# Unscramble the word: upjm
# Your answer: jump
# Correct!
# Unscramble the word: uebl
# Your answer: blue
# Correct!
# Unscramble the word: sked
# Your answer: desk
# Correct!
# Unscramble the word: leov
# Your answer: love
# Correct!
# Unscramble the word: gson
# Your answer: song
# Correct!

# Level 1 over!
# Score for Level 1: 7/7
# Enter 'next' to go to the next level or 'exit' to quit: next

# Level 2
# -------------
# Unscramble the word: eymkno
# Your answer: monkey
# Correct!
# Unscramble the word: ragoen
# Your answer: orange
# Correct!
# Unscramble the word: azber
# Your answer: zebra
# Correct!
# Unscramble the word: hgkiin
# Your answer: hiking
# Correct!
# Unscramble the word: elvnee
# Your answer: eleven
# Correct!
# Unscramble the word: aanban
# Your answer: banana
# Correct!
# Unscramble the word: ndoeky
# Your answer: donkey
# Correct!

# Level 2 over!
# Score for Level 2: 7/7
# Enter 'next' to go to the next level or 'exit' to quit: next

# Level 3
# -------------
# Unscramble the word: eodlwegnk
# Your answer: knowledge
# Correct!
# Unscramble the word: praivcsajt
# Your answer: javascript
# Correct!
# Unscramble the word: rlcoayvabu
# Your answer: vocabulary
# Correct!
# Unscramble the word: mpgmoiangrr
# Your answer: programming
# Correct!
# Unscramble the word: ictnynpreo
# Your answer: encryption
# Correct!
# Unscramble the word: ohibxnopae
# Your answer: xenophobia
# Correct!
# Unscramble the word: mtsiacaethm
# Your answer: ssssd
# Wrong!

# Level 3 over!
# Score for Level 3: 6/7

# Game Over, rahul!
# Total Score: 20/21