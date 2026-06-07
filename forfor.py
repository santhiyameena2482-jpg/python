# Get input for number a and b.
#     print the number between a and b
a=int(input())
b=int(input())
for i in range(a+1,b):
    print(i)

# print even number between 1 to 10.
for i1 in range (1,11):
    if(i1%2==0):
        print(i1)

    # count the number of even numbers between 1 to 10
    count=0
    for i2 in range(1,11):
       if(i2%2==0):
          count=count+1
    print(count)

# count the number of odd and even nnumbers between 1 to 10 and 
# print it.

e_count=0
o_count=0
for i3 in range(1,11):
    if(i3%2==0):
        e_count=e_count+1
    else:
       o_count=o_count+1
print(e_count)
print(o_count)
