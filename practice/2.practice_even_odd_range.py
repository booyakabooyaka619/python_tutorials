a = int(input("Enter the starting number : "))
b = int(input("Enter the last number : "))
c = input("Would you like a list of even numbers or odd numbers in your defined range : ").lower()
l = []

if(c=="even"):
    for i in range (a,b+1):
        if(i%2 == 0):
            l.append(i)
            i +=1
elif(c=="odd"):
    for i in range (a,b+1):
        if(i%2 == 1):
            l.append(i)
            i +=1       
print(l)