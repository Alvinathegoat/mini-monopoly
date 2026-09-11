FWD = Event()
LT = Event()
RT = Event()
myVariable = 0
current_space_number = 0
dice1 = 0
dice2 = 0
spaces_to_move = 0

def cpmplete_task():
    global my_event, FWD, LT, RT, myVariable, current_space_number, dice1, dice2, spaces_to_move
    pass

def when_started1():
    global my_event, FWD, LT, RT, myVariable, current_space_number, dice1, dice2, spaces_to_move
    pass

def FWD_callback_0():
    global my_event, FWD, LT, RT, myVariable, current_space_number, dice1, dice2, spaces_to_move
    pass

def FWD_callback_1():
    global my_event, FWD, LT, RT, myVariable, current_space_number, dice1, dice2, spaces_to_move
    pass

def LT_callback_0():
    global my_event, FWD, LT, RT, myVariable, current_space_number, dice1, dice2, spaces_to_move
    pass

def LT_callback_1():
    global my_event, FWD, LT, RT, myVariable, current_space_number, dice1, dice2, spaces_to_move
    pass

def RT_callback_0():
    global my_event, FWD, LT, RT, myVariable, current_space_number, dice1, dice2, spaces_to_move
    pass

def RT_callback_1():
    global my_event, FWD, LT, RT, myVariable, current_space_number, dice1, dice2, spaces_to_move
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
