class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        # self.email = fname + "." + lname + "@email.com"
        # self.name = fname + " " + lname

    # def fullname(self):
    #     return '{} {}'.format(self.fname, self.lname)
    
    # def email(self):
    #     return '{}.{}.@email.com'.format(self.fname, self.lname)

    @property
    def fullname(self):
        return f"{self.fname} {self.lname}"
    
    # allows to get the email based on first name and last name
    @property
    def email(self):
        return f"{self.fname}.{self.lname}@gmail.com"
    
    # allows us to get the first name and last name based on email
    @email.setter
    def email(self,value):
        self.fname,self.lname = value.split("@")[0].split(".")

a = Employee("sunny","hora")
a.fname = "ronak"
a.lname = "singh"
a.email = "sunpreet.singh@gmail.com"

# print(a.fname)
# print(a.lname)
# print(a.fullname())
# print(a.email())
print(a.fullname)
print(a.email)