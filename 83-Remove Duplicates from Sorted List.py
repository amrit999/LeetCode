# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        node = head
        next_node = head.next
        while node.next is not None:
            if node.val == next_node.val:
                node.next = next_node.next
                next_node = node.next
            else:
                node = next_node
                next_node = node.next
        return head