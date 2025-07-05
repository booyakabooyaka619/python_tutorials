word = "donkey"

with open("p4.txt" , "r") as f:
    content = (f.read()).lower()

contentNew = content.replace(word, "######")

if(word in content):
    with open("p4.txt", "w") as f:
        f.write(contentNew)