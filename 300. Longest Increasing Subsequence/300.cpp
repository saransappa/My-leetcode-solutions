class Solution {
public:
    int max(int a,int b){
        if(a>b)return a;
        else return b;
    }
    int lengthOfLIS(vector<int>& nums) {
        if(nums.size()==0)return 0;
        int dp[nums.size()];
        int maxi=1;
        for(int i=0;i<nums.size();i++)dp[i]=1;
        for(int i=1;i<nums.size();i++){
            for(int j=0;j<i;j++){
                if(nums[j]<nums[i]){
                    dp[i] = max(dp[i],dp[j]+1);
                    maxi = max(maxi,dp[i]);
                }
            }
        }
        return maxi;
    }
};