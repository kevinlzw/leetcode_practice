# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        front = None
        tmp = head
        while tmp:
            next_head = tmp.next
            tmp.next = front
            front = tmp
            tmp = next_head
        return front
