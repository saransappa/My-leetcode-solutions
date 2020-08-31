class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int maxi = 0;
        for(auto i:candies){
            maxi  = max(maxi,i);
        }
        //cout<<maxi;
        vector<bool> v;
        for(auto i: candies){
            if (i+extraCandies >= maxi)v.push_back(true);
            else v.push_back(false);
        }
        return v;
    }
};