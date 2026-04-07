# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        temp = None
        while cur!=None:
            after = cur.next
            cur.next=temp
            temp = cur.next
            temp = cur
            cur=after
        return temp
