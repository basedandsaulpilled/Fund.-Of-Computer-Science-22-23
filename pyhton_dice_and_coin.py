'''#this is a comment
this is a comment too
#flip a coin program
from random import choice, random

#1st method use random.random()
#coin_flip_with_random = "france" if random() > 0.5 else "italy"

#2nd method random.choice()
coin_flip_with_choice = choice(["italy", "paris", "Rome", "Canada", "Alaska", "sydney", "los angeles", "cancun", "acapulco", "mexico city", "Miami"])

print(coin_flip_with_choice)'''
#roll a dice
#1st import to your libraries
from random import randint
repeat = True
while repeat:
  print("you rolled", randint (1,6))
  print("do you want to try again?")
  repeat = ("y" or "yes") in input().lower()
