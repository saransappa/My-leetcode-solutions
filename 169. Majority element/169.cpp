class Solution {
public:
    int majorityElement(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int k=INT_MIN;
        int n=nums.size();
        for(int i=0;i+n/2<n;i++){
            if(nums.at(i)==nums.at(i+n/2)){
                k=nums.at(i);
                break;
            }
        }        
        return k;
    }
};