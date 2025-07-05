num = int(input("Enter a number : "))

while(num % 2 == 0):
    print(f"The number {num} is not a prime number")
    break
else:
    print(f"The number {num} is a prime number")

