#Name: Eden Xie
#Class: 6th Hour
#Assignment: SC4

#You have been transferred to a new team working on a mobile game that allows you to dress up a
#model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.
import math
b=int(input("How many players?"))
empty=0
for i in range(1,b):
    a=int(input("Rate the model:"))
    while a>5 or a<1:
        a = int(input("Invalid input, rate the model again:"))
    else:
        empty+=a
print(empty/(b-1))