class Solution:
    def compareTwoWords(self, a: str, b: str, delete: set) -> set:
        i = 0
        word_size = len(a)
        while i < len(a):
            if i not in delete:
                if a[i] < b[i]:
                    break
                elif a[i] > b[i]:
                    delete.add(i)
            i += 1
        return delete
    def minDeletionSize(self, strs: List[str]) -> int:
        i, j = 0, 1
        delete = set()
        delete_size = 0
        word_size = len(strs[0])
        list_size = len(strs)
        while j < list_size:
            delete = self.compareTwoWords(strs[i], strs[j], delete)
            if delete_size != len(delete):
                delete_size = len(delete)
                i = 0
                j = 1
                continue

            if len(delete) >= word_size:
                return word_size
            j += 1
            i += 1
        return len(delete)
