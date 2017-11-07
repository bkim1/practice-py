class Node:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left = left_child
        self.right = right_child


import collections

def print_levels(root):
    if root is None:
        return
    queue = collections.deque()
    queue.append(root)

    while len(queue):
        node = queue.popleft()
        print(node.data,end=' ')

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    
    print()


if __name__ == "__main__":
    root = Node(5, Node(3, right_child=Node(4)), Node(7,left_child=Node(6)))

    print_levels(root)