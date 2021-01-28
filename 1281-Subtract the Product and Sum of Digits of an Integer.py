class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        add = 0
        mul = 1
        for digit in str(n):
            add = add + int(digit)
            mul = mul*int(digit)
        return mul - add