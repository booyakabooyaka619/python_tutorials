with open("p6.txt" , "r") as f:
    word = (f.read()).lower()

if ("python" in word):
    print("python found")
else:
    print("python not found")