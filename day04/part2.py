with open('input.txt') as f:
    lines = f.readlines()
    count_total = 0
    not_overlapping_count = 0
    for line in lines:
        count_total += 1
        first, second = line.strip().split(',')
        first_start, first_end = [int(n) for n in first.split('-')]
        second_start, second_end = [int(n) for n in second.split('-')]
        if first_end < second_start or second_end < first_start:
            not_overlapping_count += 1
        
    print(count_total-not_overlapping_count)
