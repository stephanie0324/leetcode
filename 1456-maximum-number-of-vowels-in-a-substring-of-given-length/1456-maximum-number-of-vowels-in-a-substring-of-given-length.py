class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        l, vowelCount, maxCount = 0, 0, 0

        for r in range(len(s)):

            # close window
            if r - l + 1 > k:
                if s[l] in vowels:
                    vowelCount -= 1
                l += 1

            # open window
            if s[r] in vowels:
                    vowelCount += 1
                    maxCount = max(maxCount, vowelCount)
        return maxCount
        