#Name: Eden Xie
#Class: 6th Hour
#Assignment: HW16


#1. import the "random" library
import random
#2. print "Hello World!"
print("Hello World!")
#3. Create three variables named a, b, and c, and allow the user to input an integer for each.
a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
c=int(input("Enter another number:"))
#4. Add a and b together, then divide the sum by c. Print the result.
d=((a+b)/c)
print(d)
#5. Round the result from #3 up or down, and then determine if it is even or odd.
print(round(d))
if d%2==0:
    print("even")
else:
    print("odd")
#6. Create a list of five different random integers between 1 and 10.
num=[random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10)]
#7. Print the 4th number in the list.
print(num[3])
#8. Append another integer to the end of the list, also random from 1 to 10.
num.append(random.randint(1,10))
#9. Sort the list from lowest to highest and then print the 4th number in the list again.
num.sort()
print(num[3])
#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.
i=1
while i<=100:
    i+=1
    print(i)
#11. Create a list containing the names of five other students in the classroom.
name=["Owyn","Owen","Jacob","Benson","Nate"]
#12. Create a for loop that individually prints out the names of each student in the list.
for i in name:
    print(i)
#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.
for i in range(1,100,1):
    print(i)
    if i%10==0:
        break
#14. Free space. Do something creative. :)
import time
green="green is not a creative color"
for i in green:
    time.sleep(0.2)
    print(i)