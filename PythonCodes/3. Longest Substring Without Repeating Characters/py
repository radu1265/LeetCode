'''
Given a string s, find the length of the longest substring without repeating characters.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        queue = []
        aux_max = 0
        max = 0
        for elem in s:
            if elem in queue:
                aux_max = len(queue)
                
                if (aux_max > max):
                    max = aux_max

#               dequeue until the doubled elem
                while elem in queue:
                    queue.pop(0)

            queue.append(elem)            
            
#             check for the last element added in the queue
    
        if len(queue) > max:
            return len(queue)
        
        return max
