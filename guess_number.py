#required modules
import random
#creating the number which stores random number
num = random.randint(1,10)
#creating variable which will take user's input
user_num = int(input("Guess a number between 1 and 10: "))
#creating the loop for the game 
if num!=user_num:
    print("Sorry,guess it again")
    user_num = int(input("Guess a number between 1 and 10: "))
print("Congrats you have won the game ✨")