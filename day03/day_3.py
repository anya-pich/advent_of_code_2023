with open('day_3.txt') as f:
    lines = f.readlines()
    total = 0
    for line in lines:
        middle = len(line.strip())//2
        first_half = set(line[:middle])
        second_half = set(line[middle:])
        dupe = first_half.intersection(second_half).pop()

        unicode = ord(dupe)
        if unicode > 96: # a-z
            priority = unicode - 96
        else: # A-Z
            priority = unicode - 64 + 26
        total += priority
    print(total)