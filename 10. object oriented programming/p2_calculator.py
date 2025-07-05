class calculator:
    def square(self, n):
        self.n = n
        print(f"The square of the {n} is {n*n}")
        print(f"The cube of the {n} is {n**3}")
        print(f"The squareroot of the {n} is {n**1/2}")


a = calculator()
b = int(input("Enter a number :"))
a.square(b)
