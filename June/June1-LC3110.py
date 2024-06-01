class Solution:
    def scoreOfString(self, s: str) -> int:
        mySum = 0
        for i in range(len(s)-1):
            mySum += abs(ord(s[i+1])-ord(s[i]))
        return mySum
