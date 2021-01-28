class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = []
        for item in nums:
            if item in l:
                l.remove(item)
            else:
                l.append(item)
        return l.pop()