class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        map<int,int> visited;
        for(int i=1;i<=n;i++){
            visited[i] = 0;
        }
        map<int,vector<int>> adj;
        map<pair<int,int>,int> dist;
        for(vector<int> v: times){
            adj[v[0]].push_back(v[1]);
            dist[make_pair(v[0],v[1])]=v[2];
        }
        queue<int> q;
        q.push(k);
        int d = 0;
        map<int,int> time;
        set<int> s;
        s.insert(k);
        int prev = k;
        visited[k] = 1;
        for(int i=1;i<=n;i++){
            if(i!=k)time[i] = INT_MAX;
        }

        int count = 0;
        while(q.size()>0){
            int z = q.front();
            for(int i : adj[z]){
                if(visited[i]==0){
                    q.push(i);
                    visited[i] =1;
                }
            }
            visited[z] =2;
            count++;
            q.pop();
        }
        for(int i=1;i<=n;i++){
            visited[i] = 0;
        }
        while(s.size()<count){
            for(int i:adj[prev]){
                time[i] = min(time[prev] + dist[make_pair(prev,i)],time[i]);
            }
            int min_val = INT_MAX;
            int min_ind = 0;
            for(int i=1;i<=n;i++){
                if(visited[i]==0){
                    if(time[i]<min_val){
                        min_val = time[i];
                        min_ind = i;
                    }
                }
            }
            visited[min_ind] = 1;
            prev = min_ind;
            s.insert(prev);
        }
        int max_time = 0;
        for(int i=1;i<=n;i++){
            if(visited[i]==0)return -1;
            else{
                max_time = max(max_time,time[i]);
            }
        }
        return max_time;
    }
};