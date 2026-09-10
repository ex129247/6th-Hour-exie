#Name: Eden Xie
#Class: 6th Hour
#Assignment: HW6


#1. Create a list with 9 different numbers inside.
FirstList=[1,2,3,4,5,6,7,8,9]
#2. Sort the list from highest to lowest.
FirstList.sort(reverse=True)
#3. Create an empty list.
Empty=[]
#4. Remove the median number from the first list and add it to the second list.
x=FirstList.pop(4)
Empty.append(x)
#5. Remove the first number from the first list and add it to the second list.
y=FirstList.pop(0)
Empty.append(y)
#6. Print both lists.
print(FirstList, Empty)
#7. Add the two numbers in the second list together and print the result.
z=Empty[0]+Empty[1]
print(z)
#8. Move the number back to the first list (like you did in #4 and #5 but reversed).
FirstList.append(z)
#9. Sort the first list from lowest to highest and print it.
FirstList.sort()
print(FirstList)