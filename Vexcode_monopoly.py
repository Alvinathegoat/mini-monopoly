screen_precision = 0
console_precision = 0
myVariable = 0
current_space_number = 0
dice1 = 0
dice2 = 0
spaces_to_move = 0
right_turn = Event()
FWD = Event()
LT = Event()
RT = Event()
left_turn = Event()

def complete_task():
    global myVariable, current_space_number, dice1, dice2, spaces_to_move, right_turn, FWD, LT, RT, left_turn, screen_precision, console_precision
    brain.screen.print(str("Landed on space") + str(current_space_number))
    brain.screen.next_row()
    wait(1, SECONDS)
    if current_space_number == 1:
        # Space = GO
        for repeat_count in range(4):
            left_turn.broadcast_and_wait()
            wait(5, MSEC)
    elif current_space_number == 4:
        # Space = Jail
        wait(3, SECONDS)
    elif current_space_number == 7:
        # Space = Free parking
        wait(5, SECONDS)
    elif current_space_number == 10:
        # Space = Go to Jail
        pass
    else:
        # Space = Blue 1 or 2, Green 1 or 2, Yellow 1 or 2, or Red 1 or 2
        pass

def play_game():
    global myVariable, current_space_number, dice1, dice2, spaces_to_move, right_turn, FWD, LT, RT, left_turn, screen_precision, console_precision
    while True:
        roll_dice()
        move()
        complete_task()
        brain.screen.set_cursor(1, 1)
        wait(5, MSEC)

def move():
    global myVariable, current_space_number, dice1, dice2, spaces_to_move, right_turn, FWD, LT, RT, left_turn, screen_precision, console_precision
    brain.screen.print(str("Moving") + str(str(spaces_to_move) + str("spaces!")))
    brain.screen.next_row()
    for repeat_count2 in range(int(spaces_to_move)):
        right_turn.broadcast_and_wait()
        current_space_number = current_space_number + 1
        if current_space_number > 12:
            current_space_number = 1
        if current_space_number == 1:
            right_turn.broadcast_and_wait()
            if current_space_number == 4:
                right_turn.broadcast_and_wait()
            if current_space_number == 7:
                right_turn.broadcast_and_wait()
            if current_space_number == 10:
                right_turn.broadcast_and_wait()
        wait(5, MSEC)

def roll_dice():
    global myVariable, current_space_number, dice1, dice2, spaces_to_move, right_turn, FWD, LT, RT, left_turn, screen_precision, console_precision
    dice1 = int(round(urandom.uniform(1, 4), 2))
    brain.screen.print(str("Rolled a:") + str(dice1))
    brain.screen.next_row()
    dice2 = int(round(urandom.uniform(1, 4), 2))
    brain.screen.print(str("Rolled a:") + str(dice2))
    brain.screen.next_row()
    spaces_to_move = dice1 + dice2

def when_started1():
    global myVariable, current_space_number, dice1, dice2, spaces_to_move, right_turn, FWD, LT, RT, left_turn, screen_precision, console_precision
    current_space_number = 1
    play_game()

def FWD_callback_0():
    global myVariable, current_space_number, dice1, dice2, spaces_to_move, right_turn, FWD, LT, RT, left_turn, screen_precision, console_precision
    pass

def FWD_callback_1():
    global myVariable, current_space_number, dice1, dice2, spaces_to_move, right_turn, FWD, LT, RT, left_turn, screen_precision, console_precision
    pass

def LT_callback_0():
    global myVariable, current_space_number, dice1, dice2, spaces_to_move, right_turn, FWD, LT, RT, left_turn, screen_precision, console_precision
    pass

def LT_callback_1():
    global myVariable, current_space_number, dice1, dice2, spaces_to_move, right_turn, FWD, LT, RT, left_turn, screen_precision, console_precision
    pass

def RT_callback_0():
    global myVariable, current_space_number, dice1, dice2, spaces_to_move, right_turn, FWD, LT, RT, left_turn, screen_precision, console_precision
    pass

def RT_callback_1():
    global myVariable, current_space_number, dice1, dice2, spaces_to_move, right_turn, FWD, LT, RT, left_turn, screen_precision, console_precision
    pass

# system event handlers
FWD(FWD_callback_0)
FWD(FWD_callback_1)
LT(LT_callback_0)
LT(LT_callback_1)
RT(RT_callback_0)
RT(RT_callback_1)
# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

when_started1()
