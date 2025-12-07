class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]
        for string in strs[1:]:
            aux = ""
            for f_letter, s_letter in zip(pref, string):
                if f_letter == s_letter:
                    aux += f_letter
                else: break
            pref = aux
        return pref
