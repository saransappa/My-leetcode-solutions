class Solution {
    public String longestCommonPrefix(String[] strs) {
        Trie trie = new Trie();
        for(String s:strs){
            if(s.equals(""))return "";
            trie.insert(s);
        }
        return trie.lcp();
    }
}

class TrieNode{
    public boolean isEndOfWord;
    public HashMap<Character,TrieNode> list;
    public TrieNode(){
        this.isEndOfWord = false;
        list = new HashMap<Character, TrieNode>();
    }
}

class Trie{
    TrieNode root;
    public Trie(){
        root= new TrieNode();
    }
    
    public void insert(String s){
        TrieNode temp = root;
        for(int i=0;i<s.length();i++){
            char t = s.charAt(i);
            if(temp.list.get(t)!=null)temp = temp.list.get(t);
            else {
                temp.list.put(t,new TrieNode());
                temp = temp.list.get(t);
            }
        }
        temp.isEndOfWord = true;
    }
    
    public String lcp(){
        TrieNode temp = root;
        String alpha = "abcdefghijklmnopqrstuvwxyz";
        String ans = "";
        while(true){
            int c = 0;
            char temp_i='*';
            for(int i=0;i<26;i++){
                if(temp.list.get(alpha.charAt(i))!=null){
                    c++;
                    temp_i = alpha.charAt(i);
                };
            }    
            if(c==0)break;
            if(c>1 || temp.isEndOfWord)return ans;
            ans+=temp_i;
            temp = temp.list.get(temp_i);
        }
        return ans;
    }
}