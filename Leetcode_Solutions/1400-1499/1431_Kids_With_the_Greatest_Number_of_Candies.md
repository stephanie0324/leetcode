# 1431. Kids With the Greatest Number of Candies
* tags : Array
* Difficulty : Easy

# Description
* Given an integer array candies, where each candies[i] represents the number of candies the ith kid
* An integer extraCandies, denoting the number of extra candies that you have.
* Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, else false
* Note that multiple kids can have the greatest number of candies.

### Constraints:

```ruby
n == candies.length
2 <= n <= 100
1 <= candies[i] <= 100
1 <= extraCandies <= 50
```

### Example 
```ruby
Input: candies = [12,1,12], extraCandies = 10
Output: [true,false,true]
```
# Problem Solving
### Solution 1 : Greedy
Go thru all the kids and add the extra candies to see if they are the max.

```ruby
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_cnt = max(candies)
        list_of_bool = [0]*len(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies >= max_cnt:
                list_of_bool[i] = 1
        return list_of_bool
```