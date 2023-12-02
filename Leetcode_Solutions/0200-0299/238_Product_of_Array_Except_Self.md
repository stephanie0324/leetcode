# 238. Product of Array Except Self
* tags : Array, Prefix Sum
* difficulties : medium

# Description
Given an integer array nums, return an array answer such that `answer[i]` is equal to the product of all the elements of nums except `nums[i]`.

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in` O(n)` time and without using the division operation.

### Constraints:
```ruby
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
```


### Example 
Example 1:
```ruby
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```
Example 2:
```ruby
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

# Problem Solving
### Solution 1 : Left product x Right product
> Time Complexity :　O(n) , Space Complexity : O(1)

The _brute force method_ would be to manually calculate each product. Since there are n products to calculate, and each product is made up of n-1 numbers, this runs in O(n2) time.
&rarr; This method causes us to do the same calculations over and over again.  
**So instead, we'll calculate all the products to the left and right of any given element just once and reuse those calculations. This allows us to reduce the runtime to O(n).**

```ruby
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        products = [1] * length
        # create left
        for i in range(1, length):
            products[i] = products[i-1] * nums[i-1]
        # create right
        right = nums[-1]
        for i in range(length-2, -1, -1):
            products[i] *= right
            right *= nums[i]
        return product

```
