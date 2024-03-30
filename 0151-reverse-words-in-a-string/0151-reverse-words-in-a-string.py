class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        s = [word for word in s if len(word)>0]
        s.reverse()
        return ' '.join(s)