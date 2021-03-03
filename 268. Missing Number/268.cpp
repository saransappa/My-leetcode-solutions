class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int sum = 0;
        for(int i:nums)sum+=i;
        int n = nums.size();
        int ideal_sum = (n*(n+1))/2;
        return ideal_sum - sum;
    }
};