# def find_thing(n, input):
#     charset = set(input[:n])
#     for i in range(n, len(input)):
#         print(i, len(charset), charset)
#         if len(charset) == n:
#             return i
#         else:
#             print(input[i-n], input[i])
#             charset.discard(input[i-n])
#             charset.add(input[i])


with open('test.txt') as f:
    line = f.readline()
    # for i, char in enumerate(line[3:]):
    #     unique = len(set(line[i-4:i]))
    #     print(unique, i+3)  
    for i in range(13, len(line)):
        previous_fourteen = line[i-13:i+1]
        unique = len(set(previous_fourteen))
        if unique == 14:
            print(i+1)
            break

    # print(find_thing(4, line))
