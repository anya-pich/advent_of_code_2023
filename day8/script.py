from treelib import Node, Tree

with open('input.txt') as f:
    matrix = []
    lines = f.readlines()
    for line in lines:
        row = [int(char) for char in list(line.strip())]
        matrix.append(row)

    print(matrix)
    # visibility_matrix = [[0]*len(matrix[0]) for row in range(len(matrix))]
    # print(visibility_matrix)


    def rowVisibility(row):
        max_from_left = [0 for _ in row]
        max_from_right = [0 for _ in row]
        for i in range(len(row)):
            if i == 0:
                max_from_left[0] = row[0]
                max_from_right[-1] = row[-1]
            else:
                max_from_left[i] = max(row[i], max_from_left[i-1])
                max_from_right[-i-1] = max(row[-i-1], max_from_right[-i])
        visibility = [1 for _ in row]
        for i in range(1, len(row)-1):
            if row[i] <= max_from_left[i-1] and row[i] <= max_from_right[i+1]:
                visibility[i] = 0
        return visibility

    horizontal_visibility_matrix = [rowVisibility(row) for row in matrix]
    print(horizontal_visibility_matrix)

    transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    vertical_visibility_matrix = [rowVisibility(row) for row in transposed_matrix]
    transposed_vertical_visibility_matrix = [[vertical_visibility_matrix[j][i] for j in range(len(vertical_visibility_matrix))] for i in range(len(vertical_visibility_matrix[0]))]
    print(transposed_vertical_visibility_matrix)

    visible_trees = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if horizontal_visibility_matrix[row][col] == 1 or transposed_vertical_visibility_matrix[row][col] == 1:
                visible_trees += 1
    print('visible trees:', visible_trees)