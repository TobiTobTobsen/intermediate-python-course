#import modul random
import random
#add dice rolls numbers
#add user input
dice_rolls = int(input("How many times? "))
dice_side = int(input("How many sides? "))
#add sum
dice_sum = 0
#def funtion
def main(dice_side):
  roll = random.randint(1,dice_side)
  if roll == 1:
    print(f"you rolled a {roll}! Critical Fail")
  elif roll == 6:
    print(f"you rolled a {roll}! Critical Success")
  else:
    print(f"you rolled a {roll}")
  return roll

for i in range (0,dice_rolls):
  if __name__== "__main__":
    dice_sum = dice_sum + main(dice_side)

#print sum
print(f'You have rolled a total of {dice_sum}')
