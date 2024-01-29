class Solution:
    def maxLength(self, A: List[str]) -> int:
        """
        brute force:
        for each string, go through the rest of the list
        if the list elements chars are not in the current string builder, add it. 
        if it is, is it also in any of the strings after our starting string? if so, try to replace. take "cha" and "r" for example. when i come to "ers" i want that to replace the "r". 
        in my inner for loop, check each character in current string. if it is in my string builder so far, 
        """
        dp = [set()]
        for a in A:
            if len(set(a)) < len(a): continue
            a = set(a)
            for c in dp[:]:
                print(c)
                if a & c: continue
                dp.append(a | c)
            print(dp)
        return max(len(a) for a in dp)
        