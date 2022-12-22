from treelib import Node, Tree

with open('input.txt') as f:
    matrix = []
    lines = f.readlines()
    for line in lines:
        row = [int(char) for char in list(line.strip())]
        matrix.append(row)

    def score_location(matrix, row, col):
        current = matrix[row][col]
        up, down, left, right = 0, 0, 0, 0
        up_pointer = row - 1
        down_pointer = row + 1
        left_pointer = col - 1
        right_pointer = col + 1
        while up_pointer >= 0 and matrix[up_pointer][col] <= current:
            up += 1
            if matrix[up_pointer][col] >= current:
                break
            up_pointer -= 1
        while down_pointer < len(matrix) and matrix[down_pointer][col] <= current:
            down += 1
            if matrix[down_pointer][col] >= current:
                break
            down_pointer += 1
        while left_pointer >= 0 and matrix[row][left_pointer] <= current:
            left += 1
            if matrix[row][left_pointer] >= current:
                break
            left_pointer -= 1
        while right_pointer < len(matrix[0]) and matrix[row][right_pointer] <= current:

            right += 1
            if matrix[row][right_pointer] >= current:
                break
            right_pointer += 1
        return up * down * left * right

    max_score = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            score = score_location(matrix, x, y)
            max_score = max(score, max_score)
    
    print(max_score)