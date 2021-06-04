class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        start_A = headA
        start_B = headB
        while start_A or start_B:
            if start_A == start_B:
                return start_A
            if not start_A:
                start_A = headB
            else:
                start_A = start_A.next
            if not start_B:
                start_B = headA
            else:
                start_B = start_B.next
