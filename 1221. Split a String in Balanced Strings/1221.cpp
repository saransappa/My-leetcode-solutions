class Solution {
public:
    int balancedStringSplit(string s) {
        int count = 0;
        int x = 0;
        for(int i=0;i<s.size();i++){
            if(x==0)count++;
            if(s[i]=='R')x++;
            else x--;
        }
        return count;
    }
};