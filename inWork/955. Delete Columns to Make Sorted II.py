class Solution:
    def compareTwoWords(self, a: str, b: str) -> List[int]:
        i = 0
        delete = []
        word_size = len(a)
        while i < len(a):
            if a[i] < b[i]:
                break
            elif a[i] > b[i]:
                delete.append(i)
            i += 1
        return delete
    def minDeletionSize(self, strs: List[str]) -> int:
        i, j = 0, 1
        delete = 0
        word_size = len(strs[0])
        while j < word_size:
            delete += self.compareTwoWords(strs[i][delete:], strs[j][delete:])
            print(strs[i][delete:], strs[j][delete:])
            # change this with that: res = ''.join(char for i, char in enumerate(s1) if i != idx)
            if delete >= word_size:
                return word_size
            j += 1
            i += 1
        return delete
