with open('input.txt') as f:
    lines = f.readlines()
    matrix = []
    current_row = []
    row = 0
    col = 0
    i = 0
    x = 1
    for line in lines:
        line = line.strip()
        if i in [x-1, x, x+1]:
            current_row.append('#')
        else:
            current_row.append('.')
        if line == 'noop':
            i += 1
            if i == 40:
                matrix.append(current_row)
                current_row = []
                i = 0
        else:
            _, num = line.split(' ')
            i += 1
            if i == 40:
                matrix.append(current_row)
                current_row = []
                i = 0
            if i in [x-1, x, x+1]:
                current_row.append('#')
            else:
                current_row.append('.')
            i += 1
            if i == 40:
                matrix.append(current_row)
                current_row = []
                i = 0
            x += int(num)
    for row in matrix:
        print(''.join(row))