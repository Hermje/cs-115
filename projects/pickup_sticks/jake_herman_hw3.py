#Author: Jake Herman
#Section: class
#Description: players take turns selecting an amount of sticks to pick up.
#The player who picks up the last stick loses.

game_mode = int(input("Two Human Players [1] or versus Computer [2]?"))
stick_count = 20
stick_length = 5
turn = 1
game_over = False

#the redraw parameter decides whether or not the sticks are drawn when this method is called
def human(redraw = True):
    global turn, game_over
    if redraw == True:
        turn = 1
        draw_sticks();

    while game_over == False:
        sticks_taken = int(input("player {} how many sticks would you like to take (<=3)?".format(turn)))
        if sticks_taken > 3:
            print("you cant take that many!")
            #sticks are not redrawn
            human(False)
            break
        #decrements stick_count global
        take_stick(sticks_taken)
        if game_over == True:
            break
        else:
            draw_sticks()
            change_turn()

    print("player {} wins!".format(turn))

def computer():
    print("uhhh not yet attempted")

#prints out the ascii stick art
def draw_sticks():
    stick_piece = ""
    stick_count_label = ""
    #the parts (pipes) of the sticks are printed out in rows, this creates a row
    for i in range(stick_count):
        stick_piece = stick_piece + " | "
    #prints out the rows of stick pieces
    for i in range(stick_length):
        print(stick_piece)

    for i in range(1, (stick_count+1)):
        #keeps the sticks evenly spaced, once double digits are reached there could be some inconsistencies
        if i >= 10:
            stick_count_label = stick_count_label + " " + str(i)
        else:
            stick_count_label = stick_count_label + " " + str(i) + " "

    print(stick_count_label)

#changes turn from player 1 to 2, or human to computer
def change_turn():
    global turn
    if turn == 1:
        turn = 2
    else:
        turn = 1

#handles the picking up of sticks
def take_stick(count):
    global stick_count, game_over
    if count > stick_count:
        #easier to do this than to check if the number they put in was less than the sticks left, then have to restart
        count = stick_count
    stick_count -= count
    print("Player {} took {} sticks.".format(turn, count))
    print("There are {} sticks left".format(stick_count))

    if stick_count <= 0:
        game_over = True
        change_turn()

#handles the two game modes: versus a human or computer
if game_mode == 1:
    human(True)
else:
    computer()
