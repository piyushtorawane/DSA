#STACK
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack


'''We use a stack to keep track of open brackets.

When we see a closing bracket, we pop from the stack and check if it matches the expected open bracket.

If it doesn't match or the stack is empty when it shouldn't be, return False.

At the end, if the stack is empty, all brackets were matched correctly — return True.

$$$open dekh , close dikha to nikal,match nahi hua false fek,sab sahi raha true fek$$$'''
#Time compl: O(n) — One pass through the string.

#Space compl: O(n) — In worst case, all characters are open brackets.