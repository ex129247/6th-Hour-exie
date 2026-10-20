#Name: Eden Xie
#Class: 6th Hour
#Assignment: SC2


#A local health clinic is looking to add a quick BMI calculator to their website so that their
#patients can quickly input their height and weight and be told their BMI as well as their
#classification. The classifications are as follows:

# - Underweight: Less than 18.5 BMI
# - Normal Weight: 18.5 to 24.9 BMI
# - Overweight: 25 to 29.9 BMI
# - Obese: 30 or more BMI

#It is up to you to figure out the calculation for an accurate BMI reading and tying it to
#the right classification
import math
a=int(input("Give me your height(in cm):"))
b=int(input("Give me your weight(in kg):"))
c=(b/(a/100)**2)
print(c)
if c<18.5:
    print("Underweight")
elif c==18.5 or c<=24.9:
    print("Normal Weight")
elif c>=25 or c<=29.9:
    print("Overweight")
elif c>=30:
    print("Obese")