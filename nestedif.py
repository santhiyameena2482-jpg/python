# Get input for salary and age.
# If salary greater than or equal to 20000 or age
# less than or equal to 25, get input for required loan
# amount.If not print you are not eligible for loan.

# If required loan amount is less than or equal to 50,000
# print You are eligible for loan.If it is greater than 50,000
# print maximum loan amount is 50000

salary=int(input("salary:"))
age=int(input("age:"))
if(salary>=20000 or age<25):
    loan=int(input("loan:"))
    if(loan<=50000):
        print("You are eligible")
    else:
        print("Maximum amount is 50000")
else:
    print("You are not eligible") 


# get input for five subjects marks.Add all of t,And find average.
# If average mark is less than 35. Print"Additional
# class is required" else Print "You are good to go"

tamil=int(input("Tamil:"))
english=int(input("english:"))
maths=int(input("Maths:"))
science=int(input("science:"))
social=int(input("social:"))
Average=(tamil+english+maths+science+social)/5
print("average mark is:",Average)
if(Average<35):
    print("Additional class is required")
else:
    print("You are good to go")