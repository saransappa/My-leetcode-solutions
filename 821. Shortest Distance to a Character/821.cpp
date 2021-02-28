class Solution {
public:
    vector<int> shortestToChar(string s, char c) {
        vector<int> occ;
        for(int i=0;i<s.size();i++){
            if(s[i]==c){
                occ.push_back(i);
            }
        }
        vector<int> answer;
        for(int i=0;i<s.size();i++){
            int ans = INT_MAX;
            for(int j = 0;j<occ.size();j++){
                ans = min(ans,abs(i-occ[j]));
            }
            answer.push_back(ans);
        }
        return answer;
    }
};