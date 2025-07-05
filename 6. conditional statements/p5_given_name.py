names = ["ronak", "anushree", "karan"]

text = input("Enter a name : ").lower()

if(text in names):
    print(f"The name {text} is present")

else:
    print(f"The name {text} is not present")