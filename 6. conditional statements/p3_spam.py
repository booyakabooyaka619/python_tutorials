# "Make a lot of money", "buy now", "subscribe this", "click this"

text = input("Enter the text: ").lower()

if ("make a lot of money" in text or 
    "buy now" in text or 
    "subscribe this" in text or 
    "click this" in text):
    print("This is a spam")
else:
    print("This is not a spam")
