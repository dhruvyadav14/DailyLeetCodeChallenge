class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # brute force
        """
        get the smaller word. loop through small word and inside, loop through other word. 
        if char at bigWord == smallWord[i], add that to len
        """

        # smallWord,bigWord = (text1,text2) if len(text1) < len(text2) else (text2,text1)
        # maxSeq = 0
        
        # for i in range(len(smallWord)):
        #     seq = 0
        #     for bigChar in bigWord:
        #         if i < len(smallWord) and smallWord[i] == bigChar:
        #             # start a sub sequence count
        #             # lets now look at the next smallChar
        #             seq += 1
        #             i+=1
        #     maxSeq = max(seq,maxSeq)
        # return maxSeq

        # above solution is crap. try recursion

        @cache
        def helper(s1, s2, i, j):
            if i == len(s1) or j == len(s2):
                return 0
            if s1[i] == s2[j]:
                return 1 + helper(s1, s2, i + 1, j + 1)
            else:
                return max(helper(s1, s2, i+1, j),helper(s1, s2, i, j + 1))

        return helper(text1, text2, 0, 0)
        
