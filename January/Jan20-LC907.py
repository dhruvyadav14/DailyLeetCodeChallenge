class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        # first lets just do brute force. this will exceed time limit obviously
        # total = 0
        # for i in range(len(arr)):
        #     for j in range(i+1, len(arr)+1):
        #         total += min(arr[i:j])
        # return total % (10**9 + 7)


        # loop through nums
        # keep a sumArray. this will just be the min sum array 
        # look at the array up to nums
        # i get it. lets use a monotonic stack structure. 
        # the stack should be strictly non decreasing
        # loop thru num. if stack is empty, add num to stack. this is our min so far
        # next num. is it less than the top of the stack? if so, 

        A = [0]+A
        result = [0]*len(A)
        stack = [0]
        for i in range(len(A)):
            print("starting for")
            print(f"stack: {stack}")
            print(f"result: {result}")
            while A[stack[-1]] > A[i]:
                print("in while")
                stack.pop() 
            j = stack[-1]
            result[i] = result[j] + (i-j)*A[i]
            stack.append(i)
        return sum(result) % (10**9+7)

        

        

        
