# Get input for score out of 100.
#  if score is <35="poor student"
#  if score is greater than 35 but < than 70="Average student"
#  if score is greater than 70="good student" 
score=int(input())
if(score<35):
    print("Poor student")
elif(score>35 and score<70):
    print("Average Student")
else:
    print("Good student")

# Make a mini calculator
# Get input for 2 numbers a and b
# Get input from user whether to add/sub/mul/div
# If user selects add then add the two number and Print the result.
a=int(input("A:"))
b=int(input("B:"))
operation=input("add/sub/mul/div:")
if(operation=="add"):
    print(a+b)
elif(operation=="sub"):
    print(a-b)
elif(operation=="mul"):
    print(a*b)
elif(operation=="div"):
    print(a/b)

# Get a input for score percentage.Only if the percentage is greater than
# 70,get input for his name,deparment and location.Then print you are elgibile.
# if not print you are not eligible.
score1=int(input())
if(score1>70):
    name=input("enter your name:")
    department=input("enter your department:")
    print("you are eligible")
else:
    print("you are not eligible")

