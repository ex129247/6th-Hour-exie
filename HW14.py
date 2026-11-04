#Name: Eden Xie
#Class: 6th Hour
#Assignment: HW14
import random
from traceback import print_tb

#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.
i=5
while i>=0:
    print(i)
    i-=1
else:
    print("Hello World!")
#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).
x=1
while x<=30:
    x+=1
    if x%2==0:
        print(x)
#3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
#number is divisible by 3.
y=1
while y<30:
    y+=1
    if y%3==0:
        continue
    print(y)
#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.
a=random.randint(1,6)
while True:
    a = random.randint(1, 6)
    print(a)
    if a==1:
        break
#5. Create a while loop that asks for a number input until the user inputs the number 0.
while int(input("input a number."))!=0:
    if int(input("input a number."))==0:
        break
else:
    print(int(input("input a number.")))