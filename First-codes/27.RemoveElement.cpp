/*
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

    Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
    Return k.
*/
class Solution {
public:
    void removeAux(vector<int>& nums, int pas, int val, int& count) {
        if (nums[pas] != val)
                cout << "Error" << endl;
        --count;
        for (int i = pas; i < count; i++) {
            nums[i] = nums[i + 1]; 
        }
    }
    int removeElement(vector<int>& nums, int val) {
        int count = nums.size();
        int i = 0;
        int del = -1;
        for (i = 0; i < count; i++) {
            if (nums[i] == val) {
                removeAux(nums, i, val, count);
                i--;
            }
        }
        return count;
    }

};
