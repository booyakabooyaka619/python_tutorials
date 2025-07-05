f = open("poem.txt", "r")

text = f.read()

if("twinkle" in text):
    print("twinkle fould")
else:
    print("twinkle not found")