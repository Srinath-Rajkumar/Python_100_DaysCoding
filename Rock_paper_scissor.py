#code wiritten by my own knowledge
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
option_1=rock
option_2=paper
option_3=scissors
#user input
user_input=int(input("What do you choose ? 0 for rock or 1 for paper or 2 for scissors.\n"))
if(user_input==0):
  print(option_1)
elif(user_input==1):
  print(option_2)
elif(user_input==2):
  print(option_3)

#computr choice
choice_list=[option_1,option_2,option_3]
computer_choice=random.choice(choice_list)
#game logic
def game_logic():
  if(user_input==0 and computer_choice==option_1):
    print('Draw')
  elif(user_input==0 and computer_choice==option_3):
      print('You Won')
  elif(user_input==1 and computer_choice==option_2):
    print('Draw')
  elif(user_input==1 and computer_choice==option_1):
      print('You Won')
  elif(user_input==2 and computer_choice==option_3):
    print('Draw')
  elif(user_input==2 and computer_choice==option_2):
    print('You Won')
  else:
    print('you loose')
#final output2
if(user_input <=2 and user_input >=0):
  print("Computer choce :")
  print(computer_choice)
  game_logic()
else:
  print('Invaild Input')
#code wiritten by my own knowledge