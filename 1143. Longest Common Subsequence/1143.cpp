class Solution {
public:
    int abs(int a){
        if(a<0)return -1*a;
        else return a;
    }
    int max(int a,int b){
        if(a>b)return a;
        else return b;
    }
    int longestCommonSubsequence(string text1, string text2) {
        string s = text1;
        string t = text2;
        int k = abs(s.size()-t.size());
        if(s.size()>t.size()){
            for(int i=0;i<k;i++){
                t+=" ";
            }
        }
        else{
            for(int i=0;i<k;i++){
                s+=" ";
            }
        }
        int n = s.size();
        int a[n+1][n+1];
        for(int i=0;i<n+1;i++){
            a[i][0]=0;
        }
        for(int i=0;i<n+1;i++){
            a[0][i]=0;
        }
        int max_len  = INT_MIN;
        for(int i=1;i<n+1;i++){
            for(int j=1;j<n+1;j++){
                if(s[i-1] == t[j-1]){
                    a[i][j] = a[i-1][j-1] + 1;
                }
                else{
                    a[i][j] = max(a[i-1][j],a[i][j-1]);
                }
                max_len = max(a[i][j],max_len);
            }
        }
        return max_len;
    }
};