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


def find_max_rooms(schedules):
    hour_counts = [0] * 24  # init array of size 24 with all 0s    
    for s in schedules:
        hours = range(s[0], s[1])
        for h in hours:
            hour_counts[h] += 1

    return max(hour_counts)


def run_tests():
    tests = [
        ([(2,3), (1,3), (4,5), (6,9)], 2),
        ([], 0),
        ([(1,9)], 1),
        ([(1,9), (12,17)], 1),
        ([(1,2), (2,3), (3,4)], 1),
        ([(1,9), (4,23)], 2),
        ([(1,2), (1,3), (1, 4), (3,5)], 3)
    ]

    for t in tests:
        num_rooms = find_max_rooms(t[0])
        print(num_rooms == t[1], ', ', num_rooms, '-->', t[0])



if __name__ == '__main__':
    run_tests()