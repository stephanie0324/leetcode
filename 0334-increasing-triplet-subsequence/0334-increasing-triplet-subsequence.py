class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first, sec = float("inf"), float('inf')
        
        for third in nums:
            if third <= first:
                first = third
            elif third <= sec:
                sec = third
            else:
                return True
        return False