'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

'''
class Solution:
    def isValid(self, s: str) -> bool:
        p_open = f'([{{'
        p_closed = {')' : '(',
                    '}' : '{',
                    ']' : '['
        }
        queue = []
        for elem in s:
            if elem in p_open:
                queue.append(elem)
            elif elem in p_closed:
                if not queue:
                    return False
                    
                poped = queue.pop()
                if p_closed[elem] != poped:
                    return False
        if queue: return False
        return True


# OLD SOLUTION
# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         for elem in s:
#             match elem:
#                 case '{':
#                     stack.append(elem)
#                 case '}':
#                     if not stack:
#                         return False
#                     if stack[-1] is '{':
#                         stack.pop()
#                     else:
#                         return False
#                 case '[':
#                     stack.append(elem)
#                 case ']':
#                     if not stack:
#                         return False
#                     if stack[-1] is '[':
#                         stack.pop()
#                     else:
#                         return False
#                 case '(':
#                     stack.append(elem)
#                 case ')':
#                     if not stack:
#                         return False
#                     if stack[-1] is '(':
#                         stack.pop()
#                     else:
#                         return False
#         if not stack:
#             return True
#         return False
