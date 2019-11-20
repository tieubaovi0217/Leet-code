# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = l3 = ListNode(0)
        p1 = l1
        p2 = l2
        carry = 0
        while p1 != None or p2 != None:
            new_val = 0
            if p1 != None:
                new_val += p1.val
                p1 = p1.next
            if p2 != None:
                new_val += p2.val
                p2 = p2.next
            new_val += carry
            carry = new_val // 10
            l3.next = ListNode(new_val % 10)
            l3 = l3.next
        if carry > 0:
            l3.next = ListNode(carry)
            l3 = l3.next
        return head.next