from random import randint


class Train:
    def __init__(self,trainNo):
        self.trainNo = trainNo
        
    def bookTicket(self):
        print(f"Ticket booked for train number {self.trainNo} and your ticket number is {randint(22222,55555)}")

    def checkStatus(self,fro,to):
        print(f"The train {self.trainNo} is running from {fro} to {to}")

    def checkFare(self):
        print(f"The fare for train {self.trainNo} is Rs.{randint(800,1600)}")

ticket = Train(2156)
ticket.bookTicket()
ticket.checkStatus("mumbai","lucknow")
ticket.checkFare()