class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #trying to find output of 
        stack = []
        
        for i in range(len(tokens)):
            if tokens[i] != "+" and tokens[i] != "-" and tokens[i] != "*" and tokens[i] != "/":
                stack.append(tokens[i])
            
            if stack and len(stack) > 1:
                print(stack)
                if tokens[i] == "+":
                    stack.append(int(stack.pop())+ int(stack.pop()))
                    
                elif tokens[i] == "-":
                    stack.append((int(stack.pop()) - int(stack.pop()))*-1)
                    
                elif tokens[i] == "*":
                    stack.append(int(stack.pop()) * int(stack.pop()))
                    
                elif tokens[i] == "/":
                    b, a = int(stack.pop()), int(stack.pop())
                    stack.append(int(a / b))
                
                    
        print(stack)
        return int(stack[0])
        