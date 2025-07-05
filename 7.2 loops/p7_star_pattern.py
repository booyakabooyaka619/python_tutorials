num = int(input("Enter a number : "))

for i in range(0, num):
    print(" " * (num - i - 1), end="")  # correct space alignment
    print("*" * (2 * i + 1))
