class Solution {
public:
    bool isPalindrome(string s){
        int i=0,j=s.size()-1;
        while(i<j){
            if(s[i]!=s[j])return false;
            else{
                i++;
                j--;
            }
        }
        return true;
    }
    string longestPalindrome(string s) {
        string rev = "";
        int n = s.size();
        for(int i=n-1;i>=0;i--){
            rev+=s[i];
        }
        string max_len_pal = "";
        int a[n][n];
        int max = 0;
        for(int i=0;i<n;i++){
            if(s[i]==rev[0])a[0][i]=1;
            else a[0][i] = 0;
            if(a[0][i]>max){
                string ans="";
                for(int q=i-a[0][i]+1;q<=i;q++)ans+=s[q];
                if(isPalindrome(ans)){
                    max= a[0][i];
                    max_len_pal = ans;
                }  
            }
        }
        for(int i=0;i<n;i++){
            if(s[0]==rev[i])a[i][0]=1;
            else a[i][0] = 0;
        }
        
        for(int i=1;i<n;i++){
            for(int j=1;j<n;j++){
                if(s[j]==rev[i])a[i][j] = a[i-1][j-1]+1;
                else a[i][j] = 0;
                
                if(a[i][j]>max){
                    string ans="";
                    for(int q=j-a[i][j]+1;q<=j;q++)ans+=s[q];
                    if(isPalindrome(ans)){
                        max= a[i][j];
                        max_len_pal = ans;
                    }           
                }
            }
        }
        
        return max_len_pal;
    }
};