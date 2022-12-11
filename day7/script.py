from treelib import Node, Tree

with open('input.txt') as f:
    tree = Tree()
    lines = f.readlines()
    current_node = tree.create_node(identifier='/')
    for line in lines:
        parts = line.strip().split(' ')
        if parts[0] == '$':
            if parts[1] == 'cd':
                if parts[2] == '/':
                    current_node = tree.get_node('/')
                elif parts[2] == '..':
                    current_node = tree.parent(current_node.identifier)
                else:
                    current_node = [n for n in tree.children(current_node.identifier) if n.tag == parts[2]][0]
                print('current node:', current_node)
        else:
            if parts[0] == 'dir':
                tree.create_node(tag=parts[1], parent=current_node.identifier)
            else:
                tree.create_node(tag=parts[1], data=parts[0], parent=current_node.identifier)
    tree.show()

    node = tree.get_node('/')
    def measure_directory(d, sub_100000):
        size = 0
        for child in tree.children(d.identifier):
            if child.is_leaf():
                size += int(child.data)
                child.tag = 'file'
            else:
                size += measure_directory(child, sub_100000)
                child.tag = 'dir'
        d.data = size
        if size < 100000:
            sub_100000.append(size)
        return size

    sub_100000 = []
    # over_8381165 = []
    measure_directory(node, sub_100000)
    print(sub_100000)
    print(sum(sub_100000))
    # over_8381165.sort()
    # print(over_8381165[0])

    dir_sizes = [node.data for node in tree.filter_nodes(lambda n: n.tag == 'dir')]
    dir_sizes.sort()
    system_size = tree.get_node('/').data
    print('dir sizes:', dir_sizes)
    print('space used:', system_size)
    space_needed = 30000000 - (70000000 - system_size)
    print('space needed:', space_needed)
    for dir in dir_sizes:
        if dir >= space_needed:
            print('answer:', dir)
            break

    
