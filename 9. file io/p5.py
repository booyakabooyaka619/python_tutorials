words = ["donkey", "bhaiyabsdka", "nepali"]

with open("p5.txt" , "r") as f:
    content = (f.read()).lower()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("p5.txt", "w") as f:
    f.write(content)

