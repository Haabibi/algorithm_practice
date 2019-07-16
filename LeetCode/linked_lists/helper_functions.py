"""
Helper functions for visualizing linked lists
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def createLinkedList(array):
    if len(array) == 0:
        return None
    node = ListNode(array[0])
    cur_head = node
    for item in array[1:]:
        cur_head.next = ListNode(item)
        cur_head = cur_head.next
    return node


def printLinkedList(head):
    cur_head = head
    while cur_head != None:
        print(cur_head.val, end="")
        if cur_head.next != None:
            print("->", end="")
        cur_head = cur_head.next
