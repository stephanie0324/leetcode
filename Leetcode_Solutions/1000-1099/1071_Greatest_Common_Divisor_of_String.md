# 1071. Greatest Common Divisor of Strings
* tags : String, Math
* difficulties : easy

# Description
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

### Constraints:
```ruby
1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
```

### Example 
Example 1:
```ruby
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
```
Example 2:
```ruby
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
```
Example 3:
```ruby
Input: str1 = "LEET", str2 = "CODE"
Output: ""
```

Example 4:
```ruby
Input: str1 = "ABCDEF", str2 = "ABC" # str1 != ABC+ABC
Output: ""
```

# Problem Solving
### Solution 1 : Recursion
> Time Complexity :　O(n) , Space Complexity : O(n)

We can use a recursive approach to find the greatest common divisor of two strings.    
* Approach  
Basically the str1 and str2 is the concat of substring $s'$, which implies that str1 = $s'+s'+....'$ and so does str2  
  * If `str1 + str2 != str2 + str1`, then there's no common divisor possible. So, we return an empty string "".
  * If the lengths of str1 and str2 are equal, and the concatenated strings are equal, then str1 (or str2) itself is the greatest common divisor, and we return str1 (or str2).
  * If the length of str1 is greater than the length of str2, it means that str1 contains str2 as a prefix. In this case, we recurse with the substring of str1 after removing (slicing) the prefix that matches str2.
  * If the length of str2 is greater than the length of str1, it means that str2 contains str1 as a prefix. In this case, we recurse with the substring of str2 after removing (slicing) the prefix that matches str1.

```ruby
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ""
        if len(str1) == len(str2):
            return str1
        if len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)
        return self.gcdOfStrings(str1, str2[len(str1):])

```
