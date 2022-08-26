import random


class Garage:
    def __init__(self, spaces, tickets, current_ticket):
        self.spaces = spaces
        self.tickets = tickets
        self.current_ticket = current_ticket

    def info(self):
        ticket = random.randint(1, 100)
        print(f'This is your ticket# {ticket}')
        self.tickets.append(ticket)
        self.current_ticket[ticket] = False
        self.spaces.pop()

    def payment(self):
        amt = int(input('Please enter your ticket number: '))
        if amt in self.tickets:
            pay = input("The amount due for {amt} is $40.00. Charge account?")
            if pay.lower() == "yes":
                self.current_ticket[amt] = True
                self.spaces.append(1)
                print(f'Ticket # {amt} has been paid. Please vacate space in 15 mins')
            elif pay.lower() == "no":
                print(f'A bill will be sent to address associated with plate#. Please vacate space in 15 mins')
            else:
                print(f'Please enter valid command')
        print('Thank you and have a nice day!')

    def avail(self):
        x = 0
        for space in self.spaces:
            x += 1
        print(f'There are {x} space available')


# Garage starts with a set number of spaces.
# 1 represents a space. there are 15 spaces available

avails = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


parking = Garage(avails, [], {})


def run():
    while True:
        print('Welcome')
        parking.avail()
        start = input("Park or pay ")
        if start.lower() == "park":
            parking.info()
        elif start.lower() == "pay":
            parking.payment()
        else:
            print(f'Please make a valid selection')


run()
