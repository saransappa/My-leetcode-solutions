class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        vector <int> v;
        for(vector<int> k : accounts){
            v.push_back(accumulate(k.begin(),k.end(),0));
        }
        sort(v.begin(),v.end(),greater<int>());
        return v[0];
    }
};