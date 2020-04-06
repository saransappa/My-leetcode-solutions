class Solution {
public:
    int max(int a,int b){
        if(a>b)return a;
        else return b;
    }
    int longestPalindromeSubseq(string s) {
        string t="";
        for(int i=s.size()-1;i>=0;i--){
            t+=s[i];
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