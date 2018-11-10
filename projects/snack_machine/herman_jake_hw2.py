#Name: Jake Herman
#Section: C
#Project: Snack Machine
#Description: program describing the functions
#             of a simple vending machine


state = "A"
total_inserted = 0
snack_1 = 2
snack_2 = 4
snack_3 = 1
#stores input to manage loop
command = str(input("enter 'start' to begin: "))
snack_choice = 0

while command != "exit":
    #prevents machine from being stuck in the first state
    if command == "start" and state == "A":
        state = "B"

    if state == "B":
        #adds to total inserted so we can come back here if insufficient funds are inserted
        total_inserted = total_inserted + int(input("how much money would you like to insert? "))
        state = "C"
    elif state == "C":
        snack_choice = int(input("would you like snack 1 ($2), 2 ($2), or 3 ($3), or a refund (4)? "))
        if snack_choice == 1:
            if total_inserted >= 2:
                #checks to make sure snack is in stock
                if snack_1 > 0:
                    snack_1 -= 1
                    state = "D"
                else:
                    #if out of stock, refund and exit
                    print("out of snack 1")
                    snack_choice = 4
            else:
                print("insert more money")
                state = "B"
        elif snack_choice == 2:
            if total_inserted >= 2:
                if snack_2 > 0:
                    snack_2 -= 1
                    state = "D"
                else:
                    print("out of snack 2")
                    snack_choice = 4
            else:
                print("insert more money")
                state = "B"
        elif snack_choice == 3:
            if total_inserted >= 3:
                if snack_3 > 0:
                    snack_3 -= 1
                    state = "D"
                else:
                    print("out of snack 3")
                    snack_choice = 4
            else:
                print("insert more money")
                state = "B"
        else:
            #option 4 cancels process and restarts the machine
            print("refunding: $" + str(total_inserted))
            total_inserted = 0
            state = "A"
    elif state == "D":
        #handles money, subtracts price of each snack
        print("Dispensing snack " + str(snack_choice))
        if snack_choice == 1 or snack_choice == 2:
            total_inserted -= 2
            state = "E"
        else:
            total_inserted -= 3
            state = "E"
    elif state == "E":
        #change is returned and machine restarts
        print("returning change: $" + str(total_inserted))
        #resets manipulated variables for next user
        total_inserted = 0
        command = "start"
        state = "A"
        snack_choice = 0
