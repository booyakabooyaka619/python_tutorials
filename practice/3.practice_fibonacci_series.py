num = int(input("Enter how terms you want in the series: "))

a = 0
b = 1
l = []

for i in range(num):
    l.append(a)
    a, b = b, a + b  # Update a and b

print("Fibonacci Series:", l)
