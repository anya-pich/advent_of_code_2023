with open('input.txt') as f:
    first_line = f.readline()
    crates = list(first_line.strip('\n')[1::4])
    stacks = []
    for crate in crates:
        if crate == ' ':
            stacks.append([])
        else:
            stacks.append([crate])

    lines = f.readlines()
    for line in lines:
        if len(line) == len(first_line):
            crates = list(line.strip('\n')[1::4])
            for i, crate in enumerate(crates):
                if crate != ' ':
                    stacks[i].append(crate)
        elif len(line) == 1:
            for stack in stacks:
                stack.pop()
                stack.reverse()
        else:
            times, from_stack, to_stack = [int(n) for n in line.strip().split(' ')[1::2]]
            from_stack -= 1
            to_stack -= 1
            for time in range(times):
                moving_crate = stacks[from_stack].pop(time-times)
                stacks[to_stack].append(moving_crate)
    
    print(''.join([stack.pop() for stack in stacks]))
            
        
