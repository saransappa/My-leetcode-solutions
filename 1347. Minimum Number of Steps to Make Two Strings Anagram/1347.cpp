class Solution {
public:
    int minSteps(string s, string t) {
        map <int,int> m1, m2;
        for(int i=0;i<s.size();i++){
            m1[s[i]-'a']++;
        }
        
        for(int i=0;i<t.size();i++){
            m2[t[i]-'a']++;
        }
        int c = 0;
        for(int i=0;i<26;i++){
            c+=abs(m1[i]-m2[i]);
        }
        return c/2;
    }
};