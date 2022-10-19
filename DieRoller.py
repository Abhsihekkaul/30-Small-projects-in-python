#Dice Roll 
import random as rd

Input_Dice_Sides = int(input("Input the number of side you want in your dice : "))

Your_Die_roll = rd.randint(1,Input_Dice_Sides + 1)

print(Your_Die_roll)


