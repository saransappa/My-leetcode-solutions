class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        string s,t;
        for(string p: word1)s+=p;
        for(string p: word2)t+=p;
        if(s==t)return true;
        else return false;
    }
};