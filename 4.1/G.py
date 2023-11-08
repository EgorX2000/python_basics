def can_eat(start, finish):
    if (start[1] + 2 == finish[1] and start[0] + 1 == finish[0]) or \
       (start[0] + 2 == finish[0] and start[1] + 1 == finish[1]) or \
       (start[0] + 2 == finish[0] and start[1] - 1 == finish[1]) or \
       (start[1] - 2 == finish[1] and start[0] + 1 == finish[0]) or \
       (start[1] - 2 == finish[1] and start[0] - 1 == finish[0]) or \
       (start[0] - 2 == finish[0] and start[1] - 1 == finish[1]) or \
       (start[0] - 2 == finish[0] and start[1] + 1 == finish[1]) or \
       (start[1] + 2 == finish[1] and start[0] - 1 == finish[0]):
        return True
    else:
        return False
