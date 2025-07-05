num = int(input("Enter number of rows : "))
print("-"*35)

ask1 = int(input("What type of pattern you want \n 1. Triange \n 2. Frame \n 3. Diamond \n 4. Butterfly \n 5. Sandclock \n Enter your answer : "))
print("-"*35)
# pattern = "Triangle" if ask1 == 1 else "Frame" if ask1 == 2 else "Unknown"

if(ask1 == 1):
    ask2 = int(input(f"Do you want the triangle \n 1. Standard \n 2. Right-Angled  \n Enter your answer : "))
    print("-"*35)

    if(ask2 == 1):
        ask21 = int(input(f"Do you want the standard triangle \n 1. Straight \n 2. Reversed(Cone)  \n Enter your answer : "))
        print("-"*35)

        if(ask21 == 1):

            ask211 = int(input(f"Do you want the standard triangle (Straight) \n 1. Filled \n 2. Bordered  \n Enter your answer : "))
            print("-"*35)

            if(ask211==1):

                for i in range(0, num):
                    print(" " * (num - i - 1), end="")
                    print("*" * (2 * i + 1))

            elif(ask211 == 2):
                for i in range(0, num):
                    if(i == 0):
                        print(" " * (num - 1), end="")
                        print("*")
                    elif(i == num - 1):
                        print("*" * (num * 2 - 1))
                    else:
                        print(" " * (num - i - 1), end="")
                        print("*", end="")
                        print(" " * (2 * i - 1), end="")
                        print("*")

        elif(ask21==2):

            ask212 = int(input(f"Do you want the standard triangle (Reversed) \n 1. Filled \n 2. Bordered  \n Enter your answer : "))
            print("-"*35)

            if(ask212==1):
                for i in range(num, 0, -1):
                    print(" " * (num-i),end="")
                    print("*" * (2*i-1))

            elif(ask212 == 2):
                for i in range(num, 0, -1):
                    print(" " * (num-i),end="")
                    if(i==num):
                        print("*" * (2*i-1))
                    elif(i==1):
                        print("*")
                    else:
                        print("*",end="")
                        print(" " * (2*i-3),end="")
                        print("*")


    elif(ask2 == 2):
        ask22 = int(input(f"Do you want the right-angled triangle \n 1. Top-Left \n 2. Top-Right \n 3. Bottom-Left \n 4. Bottom-Right  \n Enter your answer : "))
        print("-"*35)

        if(ask22==1):
            ask221 = int(input(f"Do you want the Right-Angled triangle(Top-Left) \n 1. Filled \n 2. Bordered  \n Enter your answer : "))
            print("-"*35)
            if(ask221==1):
                for i in range(0, num):
                    print("*" * (i+1))

            elif(ask221==2):
                for i in range(0, num):
                    if(i==0):
                        print("*")
                    elif(i==num-1):
                        print("*" * num)
                    else:
                        print("*",end="")
                        print(" " * (i-1),end="")
                        print("*")

        if(ask22==2):
            ask222 = int(input(f"Do you want the Right-Angled triangle(Top-Right) \n 1. Filled \n 2. Bordered  \n Enter your answer : "))
            print("-"*35)
            if(ask222==1):
                for i in range(0, num):
                    print(" " * (num - i - 1),end="")
                    print("*" * (i + 1))

            elif(ask222==2):
                for i in range(0, num):
                    print(" " * (num - i - 1),end="")
                    
                    if(i==0):
                        print("*")
                    elif(i==num-1):
                        print("*" * num)
                    else:
                        print("*",end="")
                        print(" " * (i - 1),end="")
                        print("*")

        if(ask22==3):
            ask223 = int(input(f"Do you want the Right-Angled triangle(Bottom-Left) \n 1. Filled \n 2. Bordered  \n Enter your answer : "))
            print("-"*35)
            if(ask223==1):
                for i in range(0, num):
                    print(" " * (num - i - 1),end="")
                    print("*" * (i + 1))

            elif(ask223==2):
                for i in range(num, 0, -1):
                    if(i==num):
                        print("*" * i)
                    elif(i==1):
                        print("*")
                    else:
                        print("*",end="")
                        print(" " * (i - 2),end="")
                        print("*")

        if(ask22==4):
            ask224 = int(input(f"Do you want the Right-Angled triangle(Bottom-Left) \n 1. Filled \n 2. Bordered  \n Enter your answer : "))
            print("-"*35)
            if(ask224==1):
                for i in range(num, 0, -1):
                    print(" " * (num-i),end="")
                    print("*" * (i))

            elif(ask224==2):
                for i in range(num, 0, -1):
                    print(" " * (num-i),end="")

                    if(i==num):
                        print("*" * num)
                    elif(i==1):
                        print("*")
                    else:
                        print("*",end="")
                        print(" " * (i-2),end="")
                        print("*")

        

elif(ask1 == 2):

    for i in range(0, num):
        if(i == 0 or i == num - 1):
            print("*" * (num))
        else:
            print("*", end="")
            print(" " * (num - 2), end="")
            print("*")

elif(ask1 == 3):
    ask3 = int(input(f"Do you want the diamond \n 1. Filled \n 2. Bordered  \n Enter your answer : "))
    print("-"*35)

    if(ask3 == 1):
        for i in range(0, num):
            print(" " * (num - i - 1),end="")
            print("*" * (2 * i + 1))

        for i in range((num - 1), 0, -1):
            print(" " * ((num - 1) - i + 1), end="")
            print("*" * (2 * i - 1))
    
    elif(ask3 == 2):
        for i in range(0, num):
            if(i == 0):
                print(" " * (num - 1), end="")
                print("*")

            else:
                print(" " * (num - i - 1), end="")
                print("*", end="")
                print(" " * (2 * i - 1), end="")
                print("*")

        for i in range((num - 1), 0, -1):
            if(i == 1):
                print(" " * ((num-1)), end="")
                print("*")
            else:
                print(" " * ((num - 1) - i + 1), end="")
                print("*", end="")
                print(" " * (2 * i - 3), end="")
                print("*")

elif(ask1 == 4):
    ask4 = int(input(f"Do you want the butterfly \n 1. Filled \n 2. Bordered  \n Enter your answer : "))
    print("-"*35)

    if(ask4 == 1):
        for i in range(0, num):
            print("*" * (i+1),end="")
            print(" " * ((2*num-2)-(i*2)), end="")
            print("*" * (i+1))

        for i in range(num-1,0,-1):
            print("*" * i,end="")
            print(" " * ((num-i)*2),end="")
            print("*" * i)
    
    elif(ask4 == 2):
        for i in range(0,num):
            if(i==0):
                print("*",end="")
                print(" " * ((2*num-2)-(i*2)), end="")
                print("*")
            else:
                print("*",end="")
                print(" " * ((i*1-2)+1),end="")
                print("*",end="")
                print(" " * ((2*num-2)-(i*2)), end="")
                print("*",end="")
                print(" " * ((i*1-2)+1),end="")
                print("*")

        for i in range(num-1,0,-1):
            if(i==1):
                print("*",end="")
                print(" " * ((2*num-2)-(i-1)), end="")
                print("*")
            else:
                print("*",end="")
                print(" " * ((i*1-2)+1),end="")
                print("*",end="")
                print(" " * ((2*num-2)-(i*2)), end="")
                print("*",end="")
                print(" " * ((i*1-2)+1),end="")
                print("*")

elif(ask1 == 5):
    ask5 = int(input(f"Do you want the sandclock \n 1. Filled \n 2. Bordered  \n Enter your answer : "))
    print("-"*35)

    if(ask5 == 1):
        for i in range(num, 1, -1):
            print(" " * (num - i),end="")
            print("*" * (2 * i - 1))

        for i in range(0, num):
            print(" " * (num - i - 1),end="")
            print("*" * (2 * i + 1))
    
    elif(ask5 == 2):
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

else:
    print("-"*35)
    print("Unknown input")

print("-"*35)
print("\t End of the code")
print("-"*35)