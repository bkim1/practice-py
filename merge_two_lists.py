class Node:
    def __init__(self, val, n=None):
        self.value = val
        self.next = n


def merge_lists(a, b):
    """Merges two sorted linked lists in correct order"""
    if a and b:
        if a.value > b.value:
            a, b = b, a
        a.next = merge_lists(a.next, b)
    return a or b
