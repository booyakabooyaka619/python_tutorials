import random

def game():
    score = random.randint(1,100)
    print(f"Your score is {score}")

    with open("p2.txt" , "r") as f:
        text = f.read()
    
        if(text != ""):
            text = int(text)
        else:
            text = 0
    
    if(score>text):
        with open("p2.txt" , "w") as f:
            f.write(str(score))
    else:
        None
    
game()