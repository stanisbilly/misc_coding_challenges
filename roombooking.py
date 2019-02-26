'''
Given N events with the check-in time and check-out time, return the maximum 
number of rooms I need at any given time to accomodate customers

E.g. [(2, 3), (1,3), (4, 5), (6,9)]
Output: 2

Explanation: Since, we have 2 events happening concurrently, customer 1 is 
checking in at 2 and checking out at 3 while another customer is checking in 
at 1 and checking out at 3. So we will need at least 2 rooms to accomodate 
both of these customers.
'''

from collections import deque

def find_max_rooms(schedules):
    '''
    Steps + complexity (time = O(n^2), space = O(n+2k)):
    1. create a "counter" array of size 24 for the 24 hours and fill with 0
        space = 24 (k)
    2. for each schedule, expand into array of hours and increase
        the counter for the respective hour index
        time = n^2
        space = n*k (at most array of size 24 for each schedule)
    3. return the max of the counter array
        time = nlogn
    '''
    hour_counts = [0] * 24  # init array of size 24 with all 0s    
    for s in schedules:
        hours = range(s[0], s[1])
        for h in hours:
            hour_counts[h] += 1

    return max(hour_counts)


def do_overlap(tuple1, tuple2):
    '''
    Helper function to check whether two tuples (containing a range) overlap.
    '''
    if ( (tuple1[0] > tuple2[0])
        or (tuple1[0] == tuple2[0] and tuple1[1] > tuple2[1])):
        tuple1, tuple2 = tuple2, tuple1
    if (
        tuple1[0] == tuple2[0]
        or tuple1[1] > tuple2[0]
        or tuple1[1] == tuple2[1]
        ):
        return True
    else:
        return False


def find_max_rooms2(schedules):
    '''
    Steps + complexity (time = O(n^2), space = O(n)):
    1. sort the tuples by ascending 
        time = nlogn
    2. keep a second list to track the latest booked rooms
        space = n
    3. keep popping left from the schedules
        space = n
    4. for each schedule, look at the latest booked rooms,
        remove the first booked room that doesn't overlap with schedule,
        then append the schedule to the latest booked rooms
        time = n^2 (worst case: all schedules overlap)
    '''

    # schedules.sort() # sort tuples asc
    schedules = deque(schedules)
    booked_rooms = []

    while schedules:
        s = schedules.popleft()
        if not booked_rooms:
            booked_rooms.append(s)
        else:
            for r in booked_rooms:
                if not do_overlap(r, s):
                    booked_rooms.remove(r)
                    break
            booked_rooms.append(s)

    return len(booked_rooms)


def test_do_overlap():
    tests = [
        [((1,2), (1,3)), True],
        [((1,3), (1,2)), True],
        [((1,2), (2,3)), False],
        [((2,3), (1,2)), False],
    ]
    for t in tests:
        overlap = do_overlap(t[0][0], t[0][1])
        print(overlap == t[1], ',', overlap, '-->', t[0])


def run_tests(func):
    tests = [
        ([(2,3), (1,3), (4,5), (6,9)], 2),
        ([], 0),
        ([(1,9)], 1),
        ([(1,9), (12,17)], 1),
        ([(1,2), (2,3), (3,4)], 1),
        ([(1,9), (4,23)], 2),
        ([(1,2), (1,3), (1, 4), (3,5)], 3),
        ([(1,2), (1,3), (1,4), (1,5), (1,6)], 5),
        ([(1,2), (1,3), (1,4), (1,5), (1,6), (2,4)], 5)
    ]

    for t in tests:
        num_rooms = func(t[0])
        print(num_rooms == t[1], ', ', num_rooms, '-->', t[0])



if __name__ == '__main__':
    run_tests(find_max_rooms)

    # run_tests(find_max_rooms2)

    # test_do_overlap()