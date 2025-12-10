class Solution:
    # aux for star op to calculate the min repetitions of pattern
    # recive the pattern's idx position after star 
    def repeatPattern(self, p:str) -> int:
        pattern = p[0]
        count = 0
        idx_to_jump = 0
        if p[1] != '*':
            print('Error the op wasn\'t a star.')

        for elem in p[2:]:
            if elem == pattern:
                count += 1
            elif elem == '*':
                count -= 1
            else: break
            idx_to_jump += 1
            print(f'elem in pattern {elem}')
        return (count, idx_to_jump)

    def starOperator(self, s: str, p: str):
        pass
    def dotOperator(self, s: str, p: str):
        pass
    def isMatch(self, s: str, p: str) -> bool:
        s_len = len(s)
        s_idx = 0
        p_len = len(p)
        p_idx = 0

        while s_idx < s_len and p_idx < p_len:
            if s[s_idx] == p[p_idx]:
                print('good')
            # trebuie gandit indx pentru cand intra sau nu pe acest caz. ex string : b, pattern a*b e corect
            # asa ca s[s_idx] != p[p_idx], dar p[p_idx + 1] == * doar treci mai departe si ai grija la idxs
            elif p[p_idx] == '*':
                print(f'minimum number of {p[p_idx - 1]} in my pattern {self.repeatPattern(p[p_idx - 1:])}')
                self.starOperator(s[s_idx:], p[p_idx - 1:]) # si aici grija laa ce trimiti

            elif p[p_idx] == '.':
                self.dotOperator(s[s_idx:], p[p_idx:]) # mai trb gandit aici 

            else: return False

            s_idx += 1
            p_idx += 1

        if s_idx == s_len and p_idx == p_len:
            return True
        return False

