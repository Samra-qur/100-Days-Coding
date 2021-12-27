import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
images=[rock,paper,scissors]
choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if choice>2:
  print("Invalid choice")
else:
  print(f"You choose : {images[choice] }")
  computer_choice=random.randint(0,2)
  print("Computer choose:\n")
  print(f"{images[computer_choice]}")

  if choice==0 and computer_choice==1 or choice==1 and computer_choice==2 or choice==2 and computer_choice==0:
    print('You loose')
  elif choice==computer_choice:
    print("Its bet")
  else:
    print("You won")



