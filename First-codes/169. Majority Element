/*
  Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
*/

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int max = 1;
        int elem = nums[0];
        int current_max = 0;
        int current_elem = nums[0];
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == current_elem) {
                ++current_max;
            } else {
                if (current_max > max) {
                    max = current_max;
                    elem = current_elem;
                    if (max > nums.size() / 2)
                        break;
                }
                current_max = 1;
                current_elem = nums[i];
            }
            if (current_max > max) {
                max = current_max;
                elem = current_elem;
            }
        }
        return elem;
    }
};
