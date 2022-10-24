class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node = Node('root', Node('left', Node('left.left')), Node('right'))


def serialize(node_tree: Node) -> list:
    node_list = [node_tree.val]
    if node_tree.left:
        left_part = serialize(node_tree.left)
    else:
        left_part = None
    if node_tree.right:
        right_part = serialize(node_tree.right)
    else:
        right_part = None

    return node_list + [left_part] + [right_part]


def deserialize(node_list: list) -> Node:
    val = node_list[0]
    if node_list[1]:
        left_part = deserialize(node_list[1])
    else:
        left_part = None
    if node_list[2]:
        right_part = deserialize(node_list[2])
    else:
        right_part = None
    return Node(val, left_part, right_part)


assert deserialize(serialize(node)).left.left.val == 'left.left'

print(serialize(node))
