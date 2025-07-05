n=int(input("Enter the number of rows : "))

# for i in range(0, n):
#     print("*" * (i+1),end="")
#     print(" " * ((2*n-2)-(i*2)), end="")
#     print("*" * (i+1))

# for i in range(n-1,0,-1):
#     print("*" * i,end="")
#     print(" " * ((n-i)*2),end="")
#     print("*" * i)

for i in range(0,n):
    if(i==0):
        print("*",end="")
        print(" " * ((2*n-2)-(i*2)), end="")
        print("*")
    else:
        print("*",end="")
        print(" " * ((i*1-2)+1),end="")
        print("*",end="")
        print(" " * ((2*n-2)-(i*2)), end="")
        print("*",end="")
        print(" " * ((i*1-2)+1),end="")
        print("*")

for i in range(n-1,0,-1):
    if(i==1):
        print("*",end="")
        print(" " * ((2*n-2)-(i-1)), end="")
        print("*")
    else:
        print("*",end="")
        print(" " * ((i*1-2)+1),end="")
        print("*",end="")
        print(" " * ((2*n-2)-(i*2)), end="")
        print("*",end="")
        print(" " * ((i*1-2)+1),end="")
        print("*")