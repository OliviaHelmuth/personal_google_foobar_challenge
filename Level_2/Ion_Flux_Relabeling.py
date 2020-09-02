class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


current_label = 1
found_parent = -1


def build_tree(h):
    global current_label
    if (h == 0):
        return
    the_node = Node(0)
    the_node.left = build_tree(h-1)
    the_node.right = build_tree(h-1)
    the_node.val = current_label
    current_label += 1
    return the_node


def find_parent(the_node, target_value, parent=-1):
    if the_node == None:
        return
    if the_node.val == target_value:
        global found_parent
        found_parent = parent
        return
    find_parent(the_node.left, target_value, the_node.val)
    find_parent(the_node.right, target_value, the_node.val)


def solution(h, q):

    global found_parent
    my_tree = build_tree(h)
    output = []

    for item in q:
        find_parent(my_tree, item)
        output.append(found_parent)
        found_parent = -1

    return output
