class Node:
    def __init__(self, val, n=None):
        self.value = val
        self.next = n


def cycle_detect(head):
    fast = slow = head
    cycle = False

    while fast and slow:
        if fast.next is None:
            return None
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            cycle = True
            break

    if not cycle:
        return None

    slow = head
    while fast != slow:
        slow = slow.next
        fast = fast.next
    return fast
