/*
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
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
        int* duplicates = new int[pow(10,4)] ();
        if (duplicates == nullptr)
            return -1;
        int* duplicates_negative = new int[pow(10,4)] ();
        if (duplicates_negative == nullptr)
            return -1;
        int count = nums.size();
        for (int i = 0; i < count; i++) {
            cout << "mue" << endl;
            //poitive case
            if (nums[i] >= 0) {
                if (duplicates[nums[i]] == 2) {
                removeAux(nums, i, nums[i], count);
                --i;
                }
                else {
                    ++duplicates[nums[i]];
                }
            //negative
            } else {
                int aux = -nums[i];
                if (duplicates_negative[aux] == 2) {
                     removeAux(nums, i, aux, count);
                --i;
                } else {
                    ++duplicates_negative[aux];
                }
            }
        }
        delete[] duplicates;
        delete[] duplicates_negative;
        return count;
    }
};
