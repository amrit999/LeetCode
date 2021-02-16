# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None or head.next is None:
            return head
        prev_node = head
        node = prev_node.next
        new_head = None

        while head.next is not None:
            while node.next:
                prev_node = node
                node = prev_node.next

            if new_head is None:
                new_head = node

            node.next = prev_node
            prev_node.next = None
            prev_node = head
            node = prev_node.next
        return new_head
