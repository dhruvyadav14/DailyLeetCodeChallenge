class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # start from the end?
        # add operands to a operandStack and nums to a numStack
        # each operand requires two numbers
        stack=[]
        print(6//-132)
        while len(tokens)>0:
            item=tokens.pop(0)
            if item == "+":
                first=stack.pop()
                second=stack.pop()
                stack.append(first+second)
            elif item =="-":
                first=stack.pop()
                second=stack.pop()
                stack.append(second-first)
            elif item == "*":
                first=stack.pop()
                second=stack.pop()
                stack.append(first*second)
            elif item == "/":
                first=stack.pop()
                second=stack.pop()
                result=second/first
                rounded_result = math.ceil(result) if result < 0 else math.floor(result)
                stack.append(rounded_result)
            else:
                stack.append(int(item))
        return stack.pop()



            