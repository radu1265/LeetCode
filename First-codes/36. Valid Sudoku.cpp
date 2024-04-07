/*
  Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
*/

class Solution {
public:
    bool isValidCycle(const vector<char>& cycle) {
        int isOk[10] = {0}; // Store the occurrences of digits
        
        // Iterate over the cycle
        for (char c : cycle) {
            // Check if the cell is filled
            if (c != '.') {
                int digit = c - '0';
                // If the digit has already occurred in the cycle, return false
                if (isOk[digit] > 0)
                    return false;
                isOk[digit]++;
            }
        }
        return true;
    }
    
    bool isValidSudoku(vector<vector<char>>& board) {
        // Check each row
        for (int i = 0; i < board.size(); i++) {
            if (!isValidCycle(board[i]))
                return false;
        }
        
        // Check each column
        for (int j = 0; j < board[0].size(); j++) {
            vector<char> column;
            for (int i = 0; i < board.size(); i++) {
                column.push_back(board[i][j]);
            }
            if (!isValidCycle(column))
                return false;
        }
        
        // Check each 3x3 sub-box
        for (int i = 0; i < board.size(); i += 3) {
            for (int j = 0; j < board[i].size(); j += 3) {
                vector<char> subBox;
                for (int m = i; m < i + 3; m++) {
                    for (int n = j; n < j + 3; n++) {
                        subBox.push_back(board[m][n]);
                    }
                }
                if (!isValidCycle(subBox))
                    return false;
            }
        }
        
        return true;
    }
};
