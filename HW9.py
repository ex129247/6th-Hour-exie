#Name: Eden Xie
#Class: 6th Hour
#Assignment: HW9

#1. Print Hello World!
print("Hello World!")
#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers in it
Dictionary={
    "Pancake": "Waffle",
    "Evil": "Good",
    "Number": [1,2,3]
}
#3. Print the keys of the dictionary from #2.
print(Dictionary.keys())
#4. Print the values of the dictionary from #2
print(Dictionary.values())
#5. Print one of the three numbers from the list by itself
print(Dictionary["Number"][0])
#6. Using the update function, add a fourth key to the dictionary and give it a value.
Dictionary.update({"FrenchToast": "Toast"})
#7. Print the entire dictionary from #2 with the updated key and value.
print(Dictionary)
#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
Nest={
"Student_1":{
    "Name": "Owen",
    "Grade": 9,
    "Gender": "Male",
    },
    "Student_2":{
    "Name": "Jacob",
    "Grade": 9,
    "Gender": "Male",
    },
    "Student_3":{
    "Name": "Eden",
    "Grade": 9,
    "Gender": "Male",
    },
}
#9. Print the names of all three classmates on the same line.
print(Nest["Student_1"]["Name"],Nest["Student_2"]["Name"],Nest["Student_3"]["Name"])
#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.
Nest.pop("Student_3")
print(Nest)
