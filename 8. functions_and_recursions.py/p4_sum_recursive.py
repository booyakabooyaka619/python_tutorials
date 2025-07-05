num = int(input("Enter a number : "))

def sum(num):
    if(num==1):
        return 1
    else:
        return num + sum(num-1)
    
print(sum(num))