with open("p7.txt","r") as f:
   texts = f.readlines()

for i,text in enumerate(texts):
   if("python" in text):
      print(f"python found at {i}")
      