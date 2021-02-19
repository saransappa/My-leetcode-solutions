class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        int sum = 0;
        for(int i=0;i<mat.size();i++){
            if(mat.size()%2!=0){
                if(i!=mat.size()/2)sum+=mat[i][i];    
            }
            else{
                sum+=mat[i][i];
            }
        }
        int j = 0;
        for(int i=mat.size()-1;i>=0;i--){
            sum+=mat[j][i];
            j++;
        }
        return sum;
    }
};