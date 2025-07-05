class calculator:
    def square(self, n):
        self.n = n
        print(f"The square of the {n} is {n*n}")
        print(f"The cube of the {n} is {n**3}")
        print(f"The squareroot of the {n} is {n**1/2}")
    
    @staticmethod
    def greet():
        print("Hello user how are you")

a = calculator()
a.greet()
a.square(4)
