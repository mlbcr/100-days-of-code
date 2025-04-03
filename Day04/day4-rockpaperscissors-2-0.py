import random
player_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
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
choices = [rock, paper, scissors]

computer_choice = random.choice(choices)

if player_choice == 0:
    player_choice = rock
elif player_choice == 1:
    player_choice = paper
elif player_choice == 2:
    player_choice = scissors
else:
    print('Not a choice.')

print('Player choice: ')
print(player_choice)
print()
print('Computer choice: ')
print(computer_choice)
if player_choice == computer_choice:
    print("It's a draw")
elif (player_choice == rock and computer_choice == paper) or (
        player_choice == paper and computer_choice == scissors) or (
        player_choice == scissors and computer_choice == rock):
    print("You lose")
elif (player_choice == paper and computer_choice == rock) or (
            player_choice == scissors and computer_choice == paper) or (
                 player_choice == rock and computer_choice == scissors):
    print("You win")

