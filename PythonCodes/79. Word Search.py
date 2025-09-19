class Solution:
    def helper(self, board: List[List[str]], word: str, word_idx: int, l: int, r: int, used: List[Tuple[int, int]]) -> str:
        letter = word[word_idx]
        if board[l][r] != letter:
            return ''

        if word_idx == len(word) - 1:
            return letter

        line, row = len(board), len(board[0])
        word_idx += 1
        next_letter = word[word_idx]
        used.append((l,r))
        found = ''

        if (l - 1, r) not in used and 0 <= l - 1 and board[l - 1][r] == next_letter:
            found = self.helper(board, word, word_idx, l - 1, r, used)

        if not found and (l, r - 1) not in used and 0 <= r - 1 and board[l][r - 1] == next_letter:
            found = self.helper(board, word, word_idx, l, r - 1, used)

        if not found and (l + 1, r) not in used and line > l + 1 and board[l + 1][r] == next_letter:
            found = self.helper(board, word, word_idx, l + 1, r, used)
    
        if not found and (l, r + 1) not in used and row > r + 1 and board[l][r + 1] == next_letter:
            found = self.helper(board, word, word_idx, l, r + 1, used)

            
        used.pop()
        if found:
            return letter + found
        return ''

    def exist(self, board: List[List[str]], word: str) -> bool:
        for l_idx, line in enumerate(board):
            for r_idx, letter in enumerate(line):
                if self.helper(board, word, 0, l_idx, r_idx, []) == word:
                    return True
        return False
