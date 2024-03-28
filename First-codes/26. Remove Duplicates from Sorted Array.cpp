/*
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

    Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
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
    int removeDuplicates(vector<int>& nums) {
        int k = nums.size();
        int curent = nums[0];
        int count = nums.size();
        for (int i = 1; i < count; i++) {
            if (nums[i] == curent) {
                removeAux(nums, i, curent, count);
                --i;
            }
            else
                curent = nums[i];
        }
        return count;
    }
};
