class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height)-1
        max_ = 0
        
        while l<r:
            if height[l]<=height[r]:
                tmp = height[l]*(r-l)
                l+=1

            else:
                tmp = height[r]*(r-l)
                r-=1
            if tmp > max_:
                max_ = tmp
        return max_
                
        