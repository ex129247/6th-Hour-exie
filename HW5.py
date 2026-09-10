#Name: Eden Xie
#Class: 6th Hour
#Assignment: HW5

#1. Print Hello World!
print("Hello World!")
#1. Create a list with 5 strings containing 5 different names in it.
GenericList=["Wyatt","George Washington","Henry Clay","James Madison","Thomas Jefferson","Benjamin Franklin"]
#2. Append a new name onto the Name List.
GenericList.append("James Madison")
#3. Print out the 4th name on the list.
print(GenericList[3])
#4. Create a list with 4 different integers in it.
UntitledList=[1,2,3,4]
#5. Insert a new integer into the 2nd spot and print the new list.
UntitledList.insert(1,7)
print(UntitledList)
#6. Sort the list from lowest to highest and print the sorted list.
UntitledList.sort()
print(UntitledList)
#7. Add the 1st three numbers on the sorted list together and print the sum.
IntSum=UntitledList[0]+UntitledList[1]+UntitledList[2]
print(IntSum)
#8. Create a list with two strings, two integers, and two boolean values.
FinaleList=["Pancake","Waffle",6,9,True,False]
#9. Create a print statement that asks the user to input their own index value for the list on #8.
FinaleList.append(input("Enter a index value."))
print(FinaleList)