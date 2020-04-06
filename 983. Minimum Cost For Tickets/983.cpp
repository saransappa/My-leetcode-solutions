class Solution {
public:
    int max(int a,int b){
        if(a>b)return a;
        else return b;
    }
    
    int min(int a,int b){
        if(a>b)return b;
        else return a;
    }
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        bool travel[366] = {false};
        for(int i=0;i<days.size();i++){
            travel[days[i]]=true;
        }
        int dp[366] = {INT_MAX};
        dp[0]=0;
        for(int i=1;i<366;i++){
            if(travel[i]==false){
                dp[i] = dp[i-1];
            }
            else{
                dp[i] = min(min(dp[i-1]+costs[0],dp[max(0,i-7)]+costs[1]),dp[max(0,i-30)]+costs[2]);
            }
        }
        return dp[365];
    }
};