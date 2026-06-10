# Output:
# week: 1
# Day: 1
# Day: 2
# Day: 3
# week: 2
# Day: 1
# Day: 2
# Day: 3
for i in range(1,3):
    print("week:",i)
    for j in range(1,4):
        print("Day:",j)

# Output:
# 1
# 12
# 123
# 1234

for i1 in range(5):
    print()
    for j1 in range(1,i1+1):
        print(j1,end="")

# output:

# *
# **
# ***
# ****

for i2 in range(5):
    print()
    for j2 in range (1,i2+1):
        print("*",end="")