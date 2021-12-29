# AI ASSIGNMENT 2
# ROHAAN ADVANI - 111903151
# Problem Statement:
# In the water jug problem in Artificial Intelligence, we are provided with two jugs:
# one having the capacity to hold 3 gallons of water and the other has the capacity to hold 4 gallons of water.
# There is no other measuring equipment available and the jugs also do not have any kind of marking on them.
# So, the agent’s task here is to fill the 4-gallon jug with 2 gallons of water by using only these two jugs
# and no other material. Initially, both our jugs are empty.


def initial_x():
    n = int(input('How many gallons of water are there in water jug x [0-4] ? '))
    return n


def initial_y():
    n = int(input('How many gallons of water are there in water jug y [0-3] ? '))
    return n


def check_state_validity(x, y):
    if x == 0 and y == 0:
        return 1
    if x == 4 and y == 0:
        return 1
    if x == 0 and y == 3:
        return 1
    if x == 4 and y == 3:
        return 1
    if x == 1 and y == 3:
        return 1
    if x == 3 and y == 0:
        return 1
    if x == 3 and y == 3:
        return 1
    if x == 4 and y == 2:
        return 1
    if x == 0 and y == 2:
        return 1
    if x == 2 and y == 0:
        return 1
    return 0


def pouring(x, y, cost=0):
    # PERFORMANCE:
    # 1. POUR WATER INTO JUG X : +1 / +2 / +3 / +4
    # 2. POUR WATER INTO JUG Y : -1 / -2 / -3
    # 3. POUR WATER OUT OF JUG X : -1 / -2 / -3 / -4
    # 4. POUR WATER OUT OF JUG Y : +1 / +2 / +3
    # 5. NO POURING : 0
    # COST:
    # 1. COST OF EACH POUR : +1
    # 2. COST OF NO POUR : 0
    performance = 0

    while 1:
        if x == 0 and y == 0:
            print('Fill the 3-gallon jug completely (x=0, y=3)')
            x = 0
            y = 3
            performance -= 3
            cost += 1
        if x == 0 and y == 3:
            print('Pour all water from 3-gallon jug to the 4-gallon jug (x=3, y=0)')
            x = 3
            y = 0
            performance += 6
            cost += 1
        if x == 3 and y == 0:
            print('Fill the 3-gallon jug completely (x=3, y=3)')
            x = 3
            y = 3
            performance -= 3
            cost += 1
        if x == 3 and y == 3:
            print('Pour some water from the 3-gallon jug to fill the 4-gallon jug (x=4, y=2)')
            x = 4
            y = 2
            performance += 2
            cost += 1
        if x == 4 and y == 2:
            print('Empty the 4-gallon jug (x=0, y=2)')
            x = 0
            y = 2
            performance -= 4
            cost += 1
        if x == 0 and y == 2:
            print('Pour all water from 3-gallon jug to the 4-gallon jug (x=2, y=0)')
            x = 2
            y = 0
            performance += 4
            cost += 1
        if x == 2 and y == 0:
            print('Final State Reached!')
            break
        if x == 4 and y == 0:
            print('Empty the 4-gallon jug (x=0, y=0)')
            x = 0
            y = 0
            performance -= 4
            cost += 1
        if x == 4 and y == 3:
            print('Empty the 4-gallon jug (x=0, y=3)')
            x = 0
            y = 3
            performance -= 4
            cost += 1
        if x == 1 and y == 3:
            print('Empty the 4-gallon jug (x=0, y=3)')
            x = 0
            y = 3
            performance -= 1
            cost += 1
    print('Total Cost: ', cost)
    print('Total Performance: ', performance)
    return


x = initial_x()
y = initial_y()
flag = check_state_validity(x, y)
# Error Handling
while flag == 0:
    if flag == 0:
        print('Enter Valid No: of gallons')
        x = initial_x()
        y = initial_y()
        flag = check_state_validity(x, y)
pouring(x, y, cost=0)
