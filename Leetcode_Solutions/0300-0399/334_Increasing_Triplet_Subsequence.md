# 334. Increasing Triplet Subsequence
* tags : Array, Greedy
* difficulties : medium

# Description
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

### Constraints:
```ruby
1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
```


### Example 
```ruby
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
``````
# Problem Solving
### Solution 1 : Greedy 
> Time Complexity :　O(n) , Space Complexity : O(1)  

Keep track of `first` and `second`  and continue to update, always update the first if met with a smaller value, to keep the list being increasing.
```ruby
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = second = float('inf') 
        for n in nums: 
            if n <= first: 
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False

```
