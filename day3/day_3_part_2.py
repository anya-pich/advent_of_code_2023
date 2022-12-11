import itertools

with open('day_3.txt') as f:
    total = 0
    for lines in itertools.zip_longest(*[f]*3):
        elf1, elf2, elf3 = [set(line.strip()) for line in lines]
        badge = set.intersection(elf1, elf2, elf3).pop()
        
        unicode = ord(badge)
        if unicode > 96: # a-z
            priority = unicode - 96
        else: # A-Z
            priority = unicode - 64 + 26
        total += priority

    print(total)