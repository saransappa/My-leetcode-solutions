class Solution {
public:
    vector<int> decode(vector<int>& encoded, int first) {
        vector <int> v;
        int t=first;
        v.push_back(t);
        for(int i:encoded){
            t = i ^ t;
            v.push_back(t);
        }
        return v;
    }
};