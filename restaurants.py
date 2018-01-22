#!/usr/bin/env python

groups = [
        'Chloe',
        "Antonio's",
        'Mikes',
        'Korean Fried Chicken',
        'Soban',
        "Durk's",
        'Gen',
        'Den Den Cafe',
        "Harry's burger",
        'East Side pockets',
        'Skewers',
        'Wongs kitchen',
        'Flatbread',
        'Kebab and Curry',
        'Bajas',
        'Meeting Street Cafe',
        'Yans cuisine'
        ]

iteration = 0
recurrence = 0

while True:
    iteration += 1
    import random
    secure_random = random.SystemRandom()

    a = secure_random.choice(groups)
    b = random.choice(groups)
    c = random.choice(groups)
    d = secure_random.choice(groups)
    e = random.choice(groups)
    f = secure_random.choice(groups)

    if a == b == c == d == e == f:
        recurrence += 1
        if recurrence == 4:
            print('After %s iterations, group chosen is %s.' % (iteration, a))
            break
