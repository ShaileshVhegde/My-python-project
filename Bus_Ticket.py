from random import randint as ri
class BUS:
    def __init__(my,BusNO):
        my.BusNo=BusNO
    def book(my,fro,to):
        print(f"Your Bus is booked to travel {fro} to {to}")
    def status(my):
        print(f"Your Bus No {my.BusNo} is ready to bording now ")
    def ticket(my,fro,to):
        print(f"Your Bus No {my.BusNo} via {fro} to {to} and your ticket No={ri(2222,5555)} ")
t=BUS(input("Ener your bus number"))
t.book("DANDELI","BANGLORE")
t.status()
t.ticket("DANDELI","BANGLORE")