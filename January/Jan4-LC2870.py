class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        recursive backtracking?
        or actually, could this be a binary search problem? lower bound could be len(nums)//3, upperbound len(nums)//2
        nahhh i like recursive backtracking
        or WAIT, maybe just maintain a count of each element? YEAHHHH buddy thats a good one
        maintain a countMap of each element. lop through each key. if a key value is 1, return -1.
        if a key value is 2 or 3, set key value to 0, add 1 to the operation count
        if key value is > 3:
            do value%3. this result can ONLY be 0,1, or 2. 
                is it 0? then do value/3 and add that to operationCount. set key's value to 0.
                is it 1? then we MUST have EXACTLY two operations of double delete, and count//3 - 1 operations of triple delete
                is it 2? then we MUST have exactly one operation of double delete, and count//3 operations of triple delete
        bada bing bada boom, thats it
        """

        countMap=collections.Counter(nums)
        operations=0

        for key,val in countMap.items():
            if val==1:
                return -1
            elif val <=3:
                operations+=1
            else:
                modulo3=val%3
                if modulo3==0:
                    operations+=val/3
                elif modulo3==1:
                    operations+=2+(val//3)-1
                else:
                    operations+=1+(val//3)
        return int(operations)
