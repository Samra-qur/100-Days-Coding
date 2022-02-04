# Step 1: Import Modules for using functionalities in program 
from calendar import c
import random
from hangman_art import logo,stages
from hangman_words import word_list

# Step 2: Choose a random word from word_list imported above
print(logo)
chosen_word=random.choice(word_list)

#Step 3: Print chosen word for btetter understanding
print(chosen_word)

#Step 4: Store length of chosen word number of lives left for playing game
length=len(chosen_word)
lives = len(chosen_word)
#Step 5: Create  list containing blanks
d = []
for i in range(length):
    d += "_"
print(d)
#Step 6: 
end_game=False

# Step 6: Ask the User to guess the letter and iterate to get all letters until until all letters are completed. Convert input to lowercase to avoid any error in calculation
while not end_game:
    guess_word=input("Enter the guessed letter").lower()
#Step 7: If guess word in already present in d(list containing blanks), then ask user to guess again
    if guess_word in d:
        print("You have already guessed this letter, guess another !")
#Step 8: Check if guess_word is same as chosen_word and replace blank with letter
    for i in range(length):
        if chosen_word[i] == guess_word:
            d[i]=guess_word
            
#Step 9: If not same, then reduce lives with 1 , when there is no lives left then print you loose by assigning end_game as true.
    if guess_word not in chosen_word:
        print(f"You guessed wrong and lost a life")
    lives-=1
    if lives==0:
        print("You loose")
        print(chosen_word)
        end_game=True
#Step 10 : Print the list after every iteration and check if there is no blanks left in list, then user won the game by correctly guessing the word.
    print(stages[lives])
    print(d)
    if "_" not in d:
        print("You Won !")
        print(chosen_word)
        end_game = True
        

#To make game more interesting, hide the chosen_word

