num = int(input("Enter the number of rows : "))


# for i in range(num, 1, -1):
#     print(" " * (num - i),end="")
#     print("*" * (2 * i - 1))

# for i in range(0, num):
#     print(" " * (num - i - 1),end="")
#     print("*" * (2 * i + 1))

for i in range(num, 1, -1):
    print(" " * (num - i),end="")

    if(i==num):
        print("*" * (2 * i - 1))
    else:
        print("*",end="")
        print(" " * (2 * i -3),end="")
        print("*")

for i in range(0, num):
    print(" " * (num - i - 1),end="")
    if(i==0):   
        print("*")
    
    elif(i==num-1):
        print("*" * (2 * i + 1))

    else:
        print("*",end="")
        print(" " * (2 * i - 1),end="")
        print("*")