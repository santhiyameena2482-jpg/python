# Write a program to compute the sum of the first 5 
# natural numbers
a1=[]
sum1=0
for i1 in range(1,6):
    sum1=sum1+i1
print(sum1)

# write a program to read 10 numbers from the keyboard
# and find their sum and average. 
a=[]
for i in range(10):
    num=int(input())
    a.append(num)
print(a)
sum=0
for i in a:
    sum=sum+i/10
print(sum)