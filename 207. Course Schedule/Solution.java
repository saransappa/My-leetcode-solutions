class GraphNode{
    int label;
    ArrayList <GraphNode> adjlist;
    int visited;
    GraphNode(int l){
        label = l;
        adjlist = new ArrayList <GraphNode>();
        visited = -1;
    }
    
    public boolean dfs(){
        visited = 0;
        for(int i=0;i<adjlist.size();i++){
            if(adjlist.get(i).visited==-1){
                adjlist.get(i).dfs();
            }
            else if(adjlist.get(i).visited==0){
                return false;
            }
        }
        visited = 1;
        return true;
    }
    
    public void print(){
        for(int i=0;i<adjlist.size();i++){
            System.out.print(adjlist.get(i).label+"->");
        }
    }
}

class Graph{
    GraphNode [] node;
    int size;
    
    Graph(int s){
        size = s;
        node = new GraphNode[size];
        for(int i=0;i<size;i++){
            node[i]=new GraphNode(i);
        }
    }
    
    public void addEdge(int from,int to){
        node[from].adjlist.add(node[to]);
    }
    
    public boolean dfs(){
        boolean k = true;
        for(int i=0;i<size;i++){
            if(node[i].visited==-1){
                k = node[i].dfs();
                if(k==false){
                    return false;
                }
            }
            else if(node[i].visited ==0){
                return false;
            }
            
        }
        return true;
    }
    
    public void print(){
        for(int i=0;i<size;i++){
            System.out.print(node[i].label+"->");
            node[i].print();
        }
        System.out.println();
    }
}


class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        if(prerequisites.length==0 || prerequisites.length==1  )return true;
        Graph g = new Graph(numCourses);
        for(int i=0;i<prerequisites.length;i++){
            try{
                g.addEdge(prerequisites[i][0],prerequisites[i][1]);
            }
            catch(Exception e){
                e.printStackTrace();
            }
        }
        return g.dfs();
    }
}