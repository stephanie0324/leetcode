class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [1]*n
        tmp = 1        
        
        for i in range(1, n):
            ans[i] = tmp* nums[i - 1]
            tmp = ans[i]
        
        tmp = 1
        for i in range(n - 2, -1, -1):
            ans[i] *= tmp * nums[i + 1]
            tmp *= nums[i+1]
        
        return ans