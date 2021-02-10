# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        node1 = l1
        node2 = l2
        while l1 and l2:
            if node1.val <= node2.val:
                if node1.next is not None and node2.val > node1.next.val:
                    node1 = node1.next
                    continue
                l2 = l2.next
                node2.next = node1.next
                node1.next = node2
                node1 = node2
                node2 = l2

            elif node1.val > node2.val:
                l2 = l2.next
                node2.next = node1
                if node1 == l1:
                    l1 = node2
                node1 = node2
                node2 = l2

        return l1 or l2


            elif node1.val > node2.val:
                l2 = l2.next
                node2.next = node1
                if node1 == l1:
                    l1 = node2
                node1 = node2
                node2 = l2

        return l1

