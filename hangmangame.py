import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist)

# Build the hidden word: a star for each letter, but keep spaces visible
secret = []
for letter in word:
    if letter == " ":
        secret.append(" ")
    else:
        secret.append("*")

body_parts = ["head", "body", "left arm", "right arm", "left leg", "right leg"]

guessed = []    # letters the player has already tried
wrong = 0       # how many wrong guesses so far

print("Welcome to Hangman!")

# Keep playing while there are still stars and the player has body parts left
while "*" in secret and wrong < len(body_parts):
    print()
    print("Word:", "".join(secret))
    print("Guessed letters:", ", ".join(guessed))

    guess = input("Guess a letter: ").lower()

    # Only accept a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please type one letter.")
        continue

    # Don't allow the same letter twice
    if guess in guessed:
        print("You already guessed", guess, "- try a different letter.")
        continue

    guessed.append(guess)

    if guess in word:
        # Fill in the letter at every position where it appears
        for i in range(len(word)):
            if word[i] == guess:
                secret[i] = guess
        print("Yes!", guess, "is in the word.")
    else:
        print("No,", guess, "is not in the word. Added the", body_parts[wrong], "to the gallows.")
        wrong += 1
        print("Gallows:", ", ".join(body_parts[:wrong]))

# Game over: check whether they won or lost
print()
if "*" not in secret:
    print("You solved it! The word was:", word)
else:
    print("The hangman is complete. You lost! The word was:", word)
