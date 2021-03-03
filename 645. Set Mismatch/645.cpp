class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        map<int,int> m ; 
        int flag1 = false, flag2= false;
        for(int i:nums){
            m[i]++;
        }
        vector<int> ans;
        int repeat = -1, zero = -1;
        for(int i=1;i<=nums.size();i++){
            if(flag1&&flag2)break;
            if(m[i]==0){
                zero = i;
                flag1 = true;
            }
            if(m[i]==2){
                repeat = i;
                flag2 = true;
            }
        }
        ans.push_back(repeat);
        ans.push_back(zero);
        return ans;
    }
};