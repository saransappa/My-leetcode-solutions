class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        map <int,int> m;
        for(int i:arr){
            m[i]++;
        }
        vector<int> v;
        map <int,vector<int>> m2;
        set <int> s;
        for(int i:arr){
            s.insert(i);
        }
        for(int i:s){
            m2[m[i]].push_back(i);
            v.push_back(m[i]);
        }
        for(int i: v){
            if(m2[i].size()>1)return false;
        }
        return true;
    }
};