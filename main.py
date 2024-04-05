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



choose = input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

system = random.randint(0, 2)

if choose == "0":
    print(rock)
    if system == 0:
        print(f"Computer chose:\n{rock}\nDarw")
    elif system == 1:
        print(f"Computer chose:\n{paper}\nYou lose")
    elif system == 2:
        print(f"Computer chose:\n{scissors}\nYou win")
elif choose == "1":
    print(rock)
    if system == 0:
        print(f"Computer chose:\n{rock}\nYou lose")
    elif system == 1:
        print(f"Computer chose:\n{paper}\nDraw")
    elif system == 2:
        print(f"Computer chose:\n{scissors}\nYou win")
if choose == "2":
    print(rock)
    if system == 0:
        print(f"Computer chose:\n{rock}\nYou Lose")
    elif system == 1:
        print(f"Computer chose:\n{paper}\nYou win")
    elif system == 2:
        print(f"Computer chose:\n{scissors}\nDraw")
