with open('input.txt') as f:
    lines = f.readlines()
    count = 0
    for line in lines:
        first, second = line.strip().split(',')
        first_start, first_finish = [int(n) for n in first.split('-')]
        second_start, second_finish = [int(n) for n in second.split('-')]
        if first_start >= second_start and first_finish <= second_finish or first_start <= second_start and first_finish >= second_finish:
            count += 1
        
    print(count)
