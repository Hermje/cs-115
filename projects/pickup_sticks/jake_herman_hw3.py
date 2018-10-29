game_mode = input("Two Human Players [1] or versus Computer [2]?")
stick_count = 20
stick_length = 5
turn = 1
game_over = False

def human(redraw = True):
    global turn, game_over
    if redraw == True:
        turn = 1
        draw_sticks();

    while game_over == False:
        sticks_taken = input("player {} how many sticks would you like to take (<=3)?".format(turn))
        if sticks_taken > 3:
            print("you cant take that many!")
            human(False)
            break

        take_stick(sticks_taken)
        if game_over == True:
            break
        else:
            draw_sticks()
            change_turn()

    print("player {} wins!".format(turn))

def draw_sticks():
    stick_piece = ""
    stick_count_label = ""
    for i in range(stick_count):
        stick_piece = stick_piece + " | "

    for i in range(stick_length):
        print(stick_piece)

    for i in range(1, (stick_count+1)):
        if i >= 10:
            stick_count_label = stick_count_label + " " + str(i)
        else:
            stick_count_label = stick_count_label + " " + str(i) + " "
            
    print(stick_count_label)

def change_turn():
    global turn
    if turn == 1:
        turn = 2
    else:
        turn = 1

def take_stick(count):
    global stick_count, game_over
    if count > stick_count:
        count = stick_count
    stick_count -= count
    print("Player {} took {} sticks.".format(turn, count))
    print("There are {} sticks left".format(stick_count))

    if stick_count <= 0:
        game_over = True
        change_turn()


if game_mode == 1:
    human(True)
else:
    computer()
