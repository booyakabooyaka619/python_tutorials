num = int(input("Enter a number : "))

for i in range(0,num):
    print(" " * (num-i-1),end="")
    if(i==0):
        print("*")
    else:
        print("*", end="")
        print(" "*(2*i-1),end="")
        print("*")

for i in range(num-1, 0,-1):
    print(" " * (num - i),end="")
    if(i==1):
        print("*" * (2*i-1))
    else:
        print("*",end="")
        print(" " * (2*i-3),end="")
        print("*")
