# fruits = []
# a = input("Please Enter your name : ")
# b = input(f"Hello {a}, Enter your favorite fruit : ")
# fruits.append(b)
# c = input("Enter another fruit : ")
# fruits.append(c)
# d = input("Enter another fruit : ")
# fruits.append(d)
# e = input("Enter another fruit : ")
# fruits.append(e)

# print(fruits)

# num = int(input("Enter a number : "))

# if(num%2==0):
#     print(f"The number {num} is even")
# else:
#     print(f"The number {num} is odd")

# a = int(input("Enter a number : "))
# b= a**3
# print(f"The 100th square of {a} is {b}" )



# num  = int(input("Enter a number : "))
# fact = 1

# for i in range(1, num + 1):
#     fact = fact * i

# print(f"The factorial of the number {num} is ",fact)

# num = int(input("Enter a number : "))

# for i in range(0, num):
#     if(i == 0):
#         print(" " * (num - 1), end="")
#         print("*")
#     elif(i == num - 1):
#         print("*" * (num * 2 - 1))
#     else:
#         print(" " * (num - i - 1), end="")
#         print("*", end="")
#         print(" " * (2 * i - 1), end="")
#         print("*")

# for i in range(0, num):
#     print(" " * (num - i - 1),end="")
#     print("*" * (2 * i + 1))

# for i in range((num - 1), 0, -1):
#     print(" " * ((num - 1) - i + 1), end="")
#     print("*" * (2 * i - 1))


#     n=int(input("Enter the number of rows : "))

# for i in range(0, n):
#     print("*" * (i+1),end="")
#     print(" " * ((2*n-2)-(i*2)), end="")
#     print("*" * (i+1))

# for i in range(n-1,0,-1):
#     print("*" * i,end="")
#     print(" " * ((n-i)*2),end="")
#     print("*" * i)

# num = int(input("Enter the number of rows : "))

# for i in range(0, num):
#     print("*" * (i+1))

# for i in range(0, num):
#     if(i==0):
#         print("*")
#     elif(i==num-1):
#         print("*" * num)
#     else:
#         print("*",end="")
#         print(" " * (i-1),end="")
#         print("*")






# for i in range(0, num):
#     print(" " * (num - i - 1),end="")
#     print("*" * (i + 1))

# for i in range(0, num):
#     print(" " * (num - i - 1),end="")
    
#     if(i==0):
#         print("*")
#     elif(i==num-1):
#         print("*" * num)
#     else:
#         print("*",end="")
#         print(" " * (i - 1),end="")
#         print("*")





# for i in range(num,0,-1):
#     print("*" * i)

# for i in range(num, 0, -1):
#     if(i==num):
#         print("*" * i)
#     elif(i==1):
#         print("*")
#     else:
#         print("*",end="")
#         print(" " * (i - 2),end="")
#         print("*")





# for i in range(num, 0, -1):
#     print(" " * (num-i),end="")
#     print("*" * (i))

# for i in range(num, 0, -1):
#     print(" " * (num-i),end="")

#     if(i==num):
#         print("*" * num)
#     elif(i==1):
#         print("*")
#     else:
#         print("*",end="")
#         print(" " * (i-2),end="")
#         print("*")



# standard triangle

# for i in range(num, 0, -1):
#     print(" " * (num-i),end="")
#     print("*" * (2*i-1))

# for i in range(num, 0, -1):
#     print(" " * (num-i),end="")
#     if(i==num):
#         print("*" * (2*i-1))
#     elif(i==1):
#         print("*")
#     else:
#         print("*",end="")
#         print(" " * (2*i-3),end="")
#         print("*")

# for i in range(0, num):
#     print(" " * (num - i - 1), end="")  # for leading spaces
#     for j in range(1, i + 1):  # numbers from 1 to i+1
#         print(j, end="")
#     print()


# def func(num):
#     r = 1
#     for i in range(1, num + 1):
#         r = r * i
#     print(r)

# func(num)

# Without enumerate

my_list = ["apple","orange", "grapes"]

for i in range(len(my_list)):
    print(i, my_list[i])
