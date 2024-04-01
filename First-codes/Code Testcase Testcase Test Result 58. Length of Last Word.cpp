/*
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring
 consisting of non-space characters only.
*/

class Solution {
public:
    int lengthOfLastWord(string s) {
        reverse(s.begin(), s.end());
        bool erase = true;
        int indx = 0;
        int start = 0;
        for (int i = 0; i < s.length(); i ++) {
            if (s[i] == ' ') {
                if (erase){
                    start ++;
                    continue;
                }
                else{
                    indx = i;
                    break;
                }
            }
            else{
                erase = false;   
            }
        }
        if (indx == 0) {
            indx = s.length();
        }
        return indx - start;
    }
};
