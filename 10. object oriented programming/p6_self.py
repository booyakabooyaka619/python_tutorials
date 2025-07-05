from random import randint

# change self to sly
class Train:
    def __init__(sly,trainNo):
        sly.trainNo = trainNo
        
    def bookTicket(sly):
        print(f"Ticket booked for train number {sly.trainNo} and your ticket number is {randint(22222,55555)}")

    def checkStatus(sly,fro,to):
        print(f"The train {sly.trainNo} is running from {fro} to {to}")

    def checkFare(sly):
        print(f"The fare for train {sly.trainNo} is Rs.{randint(800,1600)}")

ticket = Train(2156)
ticket.bookTicket()
ticket.checkStatus("mumbai","lucknow")
ticket.checkFare()