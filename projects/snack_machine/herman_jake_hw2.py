# Name: Jake Herman
# Section: C
# Project: Snack Machine
# Description:

state = "A"
total_inserted = 0
snack_1 = 2
snack_2 = 4
snack_3 = 1
snack_names = ["Chocolate Bar", "Doritos", "Granola Bar"]
snack_choice = 0
change = 0

def main():
    global state
    if state == "A":
        command = input("input 'start' to begin: ")
        if command == "start":
            state = "B"
            main()
    elif state == "B":
        total_inserted = float(input("Insert at least $2: "))
        if total_inserted > 2:
            change = total_inserted - 2
            state = "C"
        else:
            main()
    elif state == "C":
        snack = int(input("choose a snack:\n 1: Chocolate Bar\n 2: Doritos\n 3: Granola Bar\n 4: refund"))
        if snack < 5 and snack > 0:
            snack_choice = snack
            state = "D"
            main()
    elif state == "D":
        if snack_choice < 4:
            print("dispensing " + snack_names[snack_choice - 1])
            state = "E"
            main()
        else:
            print("refunding")
            state = "A"
            main()
    elif state == "E":
        print("your change is: " + change)
        state = G
    elif state == "G":
        print("machine is off")

main()
