class Solution {
public:
    int max(int a,int b){
        if(a>b)return a;
        return b;
    }
    int findLength(vector<int>& nums1, vector<int>& nums2) {
        int a[nums2.size()][nums1.size()];
        for(int i=0;i<nums1.size();i++){
            if(nums2[0]==nums1[i])a[0][i]=1;
            else a[0][i] = 0;
        }
        for(int j=1;j<nums2.size();j++){
            if(nums1[0]==nums2[j])a[j][0]=1;
            else a[j][0] = 0;
        }
        int ans = 0;
        for(int i=1;i<nums2.size();i++){
            for(int j=1;j<nums1.size();j++){
                if(nums1[j]==nums2[i]){
                    a[i][j] = a[i-1][j-1]+1;
                    ans = max(ans,a[i][j]);
                }
                else a[i][j] = 0;
            }
        }
        return ans;
    }
};