# Get the input variable as mark.If mark>35 print pass.Else print fail 
# Sample inputnark:34
# Sample Output:
# "fail"
mark=int(input())
if(mark>35):
    print("pass")
else:
    print("fail")

 # Get input for variable income.If income is greater 
# than 7000 scholarship is available.Else not eligible for scholarship
# Sample input 
# Income:7200
# Sample Output
# "Not Eligible for scholarship"
income=int(input())
if (income>7000):
   print("Scholarship is available")
else:
    print("Not Eligible for scholarship")

# Get input for a number and check whether it is divisible by 
# both 3 and 5 or not. If yes then print, the number is divisible by 3 and 
# 5 else print the number is not divisiible by 3 and 5.
number=int(input())
if(number%3==0 and number%5==0):
    print("Divisible by both 3 and 5")
else:
    print ("Not divisible by both 3 and 5")

# Get input for a number and find it is even or odd
number1=int(input())
if(number1%2==0):
    print("even")
else:
    print("odd")

