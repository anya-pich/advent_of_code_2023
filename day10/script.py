with open('input.txt') as f:
    lines = f.readlines()
    cycle = 1
    x = 1
    running_sum = 0
    for line in lines:
        line = line.strip()
        if (cycle-20) % 40 == 0:
            signal = x * cycle
            running_sum += signal
        if line == 'noop':
            cycle += 1
        else:
            _, num = line.split(' ')
            cycle += 1
            if (cycle - 20) % 40 == 0:
                signal = x * cycle
                running_sum += signal
            cycle += 1
            x += int(num)
    print(running_sum)