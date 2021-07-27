class Solution {
public:
    map<pair<int,int>,int> visited;
        
    void dfs(int i,int j, int m,int n,vector<vector<char>>& grid){
        if(visited[make_pair(i,j)]==0){
            visited[make_pair(i,j)] = 1;
            if(i-1>=0 && grid[i-1][j]=='1'){
                dfs(i-1,j,m,n,grid);
            }
            if(i+1<m && grid[i+1][j]=='1'){
                dfs(i+1,j,m,n,grid);
            }
            if(j-1>=0 && grid[i][j-1]=='1'){
                dfs(i,j-1,m,n,grid);
            }
            if(j+1<n && grid[i][j+1]=='1'){
                dfs(i,j+1,m,n,grid);
            }
            visited[make_pair(i,j)] = 2;
        } 
    }
    int numIslands(vector<vector<char>>& grid) {
        int count = 0;
        for(int i=0;i<grid.size();i++){
            for(int j=0;j<grid[0].size();j++){
                if(grid[i][j]=='1' && visited[make_pair(i,j)]==0){
                    dfs(i,j,grid.size(),grid[0].size(),grid);
                    count++;         
                }
                
            }
        }
        return count;
    }
};