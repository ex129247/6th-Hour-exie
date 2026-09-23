#Name: Eden Xie
#Class: 6th Hour
#Assignment: HW8


#1. Import the "random" library
import random
#2. print "Hello World!"
print("Hello World")
#3. Create three different variables that each randomly generate an integer between 1 and 10
A=random.randint(1,10)
B=random.randint(1,10)
C=random.randint(1,10)
#4. Print the three variables from #3 on the same line.
print(A,B,C)
#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
D=A+2
E=B-4
F=C*1.5
#6. Print each result from #5 on the same line.
print(D,E,F)
#7. Create a list containing four variables that each randomly generate an integer between 1 and 6
List=[random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]
#8. Sort the list in #7 and print it.
List.sort()
print(List)
#9. Add together the highest three numbers in the list from #7 and print the result.
print(List[1]+List[2]+List[3])
#10. Create a list with 5 names of other students in this class and print the list.
Names=["Jacob","Owen","Owyn","Nate","Eden"]
print(Names)
#11. Shuffle the list in #10 and print the list again.
random.shuffle(Names)
print(Names)
#12. Print a random choice from the list of names from #10.]
Random=random.choice(Names)
print(Random)