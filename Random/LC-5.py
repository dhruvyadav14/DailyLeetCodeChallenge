class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        brute force is to check every possible substring starting with the current character.
        
        # maxLen = -inf
        # maxPal = ""
        # isStringPal = {}
        # x = sorted(s)
        # if x[-1] == x[0]:
        #     return s
        # for i in range(len(s)):
        #     for j in range(i+1,len(s)+1):
        #         if s[i:j] in isStringPal:
        #             isPal = isStringPal[s[i:j]]
        #         else:
        #             reversedS = s[i:j][::-1]
        #             isStringPal[s[i:j]] = True if s[i:j] == reversedS else False
        #         if isStringPal[s[i:j]] == True and len(s[i:j])>maxLen:
        #             maxLen=len(s[i:j])
        #             maxPal=s[i:j]
        # return maxPal
        

        
        i start by looking at the whole string. is it a palindrome? if so, return that string. if not, recursive call on string reduced from left side and string reduced from right side
        something like:
        longestPal(s):
            if isPalindrome(str):
                return str
            return longestPal(s[1:]) or longestPal(s[:-1])
            lets try it

        if len(s) <= 1:
            return s

        if s[::-1] == s:
            return s

        # Return the longest of the two possibilities without the first or last character
        return max(self.longestPalindrome(s[1:]), self.longestPalindrome(s[:-1]), key=len)
        """

        # lets do a two pointer solution using the same principles as above
        n = len(s)
        palStart, maxPalLen = 0, 1
        if s == s[::-1]: return s

        for i in range(0, n):
            # lets keep going through the string until we encounter a palindrome
            right = i
            while right < n and s[i]==s[right]:
                right+=1 # this is guaranteed to run once. but we need this loop for repeated chars, like aaaaaaa
            
            left = i - 1
            while left >= 0 and right<n and s[left] == s[right]: # right is peeking ahead
                left-=1
                right+=1
            
            palLen = right - left - 1 # we are guaranteed to have a pal length of 1. if our string was aa, right would be 2, left would be -1.
            if palLen > maxPalLen:
                maxPalLen=palLen
                palStart = left + 1
        return s[palStart:palStart+maxPalLen]

            
         

                    