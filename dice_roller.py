#import modul random
import random
#add dice rolls numbers
dice_rolls = 2
#add sum
dice_sum = 0

def main():
  roll = random.randint(1,6)

  print(f"you rolled a {roll}")
  return roll

for i in range (0,dice_rolls):
  if __name__== "__main__":
    dice_sum = dice_sum + main()

#print sum
print(f'You have rolled a total of {dice_sum}')
