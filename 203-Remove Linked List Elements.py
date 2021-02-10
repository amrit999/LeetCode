# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return head
        node = head
        next_node = head.next

        while node.next is not None:
            if next_node.val == val:
                node.next = next_node.next
                next_node = node.next
            else:
                node = next_node
                next_node = node.next
        if head.next == None:
            if head.val == val:
                return None
        if head.val == val:
            head = head.next
        return head
