import random

dice = {1: '⚀', 2: '⚁', 3: '⚂', 4: '⚃', 5: '⚄', 6: '⚅'}

def roll():
  d = random.randint(1, 6)
  return d

ans = input("Do you want to roll the die? (y/n) : ")

while ans.lower() in ["y", "yes"]:
  print("Die Rolled")
  d = roll()
  print(d, dice[d])
  ans = input("Do you want to roll the die again? (y/n) : ")

    