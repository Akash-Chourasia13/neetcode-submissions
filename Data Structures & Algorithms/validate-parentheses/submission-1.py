class Solution:
    def isValid(self, s: str) -> bool:
        brackets_map = {')':'(',']':'[','}':'{'}
        stack = []
        for b in s:
            if stack and b in brackets_map and stack[-1] == brackets_map[b]:
                stack.pop()
            else:    
                stack.append(b)    
        return not len(stack)        
        