class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def numbers(self):
        print(f"{self.real}i + {self.img}j")
    
    def __mul__(self, num2):
        realNew = self.real * num2.real
        imgNew =  self.img * num2.img
        return Complex(realNew, imgNew)

a = Complex(2,4)
b = Complex(3,5)
a.numbers()
b.numbers()

c = a * b
c.numbers()