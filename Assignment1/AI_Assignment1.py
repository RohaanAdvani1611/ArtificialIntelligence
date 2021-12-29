# AI ASSIGNMENT 1
# ROHAAN ADVANI - 111903151

def start_room():
    x = input('Is Vacumn Cleaner Present in room A / B : ')
    return x

def status_RoomA():
    x = input('Is room A clean / dirty : ')
    return x

def status_RoomB():
    x = input('Is room B clean / dirty : ')
    return x

def check_start_room(x):
    if x == 'A' or x == 'B':
        return 1
    return 0

def check_room_status(x):
    if x == 'clean' or x == 'dirty':
        return 1
    return 0

def cleaning(location, sA, sB, cost=0):
    # performance increments by 1 on suck operation
    # performance decrements by 1 on shift operation
    performance = 0

    # No of Rooms:
    count = 2

    while count > 0:
        # Start Room A
        if location == 'A' and sA == 'dirty':
            print(f'Performing Suck Operation in Room {location}')
            performance += 1
            sA = 'clean'
            print(f'{location} is {sA}')
            # Increase cost by 1 as Suck Operation Performed
            cost = cost + 1
        if location == 'A' and sA == 'clean':
            # No cost as no operation performed
            print(f'{location} is {sA}')
            count -= 1
        if location == 'A' and sB == 'dirty':
            location = 'B'
            print(f'Performing Shift Operation to Room {location}')
            performance -= 1
            print(f'Performing Suck Operation in Room {location}')
            performance += 1
            sB = 'clean'
            print(f'{location} is {sB}')
            # Increase cost by 2 as Shift and Suck Operations Performed
            cost = cost + 2
        if location == 'A' and sB == 'clean':
            # No cost as both rooms clean
            print(f'Both Rooms are {sB}')
            count -= 1
            break
        # Start Room B
        if location == 'B' and sB == 'dirty':
            print(f'Performing Suck Operation in Room {location}')
            performance += 1
            sB = 'clean'
            print(f'{location} is {sB}')
            # Increase cost by 1 as Suck Operation Performed
            cost = cost + 1
        if location == 'B' and sB == 'clean':
            # No cost as no operation performed
            print(f'{location} is {sB}')
            count -= 1
        if location == 'B' and sA == 'dirty':
            location = 'A'
            print(f'Performing Shift Operation to Room {location}')
            performance -= 1
            print(f'Performing Suck Operation in Room {location}')
            performance += 1
            sA = 'clean'
            print(f'{location} is {sA}')
            # Increase cost by 2 as Shift and Suck Operations Performed
            cost = cost + 2
        if location == 'B' and sA == 'clean':
            # No cost as both rooms clean
            print(f'Both Rooms are {sA}')
            count -= 1
            break
    print(f'Total cost of cleaning both rooms: {cost}')
    print(f'Total performance of cleaning both rooms: {performance}')

location = start_room()
sA = status_RoomA()
sB = status_RoomB()

flag1 = check_start_room(location)
flag2 = check_room_status(sA)
flag3 = check_room_status(sB)

# Error Handling
while flag1 == 0 or flag2 == 0 or flag3 == 0:
    if flag1 == 0:
        print('Enter valid room')
        location = start_room()
        flag1 = check_start_room(location)
    if flag2 == 0:
        print('Enter valid status of A')
        sA = status_RoomA()
        flag2 = check_room_status(sA)
    if flag3 == 0:
        print('Enter valid status of B')
        sB = status_RoomB()
        flag3 = check_room_status(sB)

cleaning(location, sA, sB, cost=0)