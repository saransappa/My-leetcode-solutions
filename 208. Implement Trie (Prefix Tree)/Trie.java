class TrieNode{
    public boolean isEndOfString;
    HashMap<Character, TrieNode> list;
    public TrieNode(){
        isEndOfString = false;
        list  = new HashMap<Character, TrieNode>();
    }
}


class Trie {
    public TrieNode root;
    /** Initialize your data structure here. */
    public Trie() {
        root = new TrieNode();
    }
    
    /** Inserts a word into the trie. */
    public void insert(String word) {
        TrieNode temp = root;
        for(int i=0;i<word.length();i++){
            char t = word.charAt(i);
            if(temp.list.get(t)!=null)temp = temp.list.get(t);
            else {
                temp.list.put(t,new TrieNode());
                temp = temp.list.get(t);
            }
        }
        temp.isEndOfString = true;
    }
    
    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        TrieNode temp = root;
        for(int i=0;i<word.length();i++){
            char t = word.charAt(i);
            if(temp.list.get(t)!=null)temp = temp.list.get(t);
            else return false;
        }
        if(temp.isEndOfString)return true;
        else return false;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        TrieNode temp = root;
        for(int i=0;i<prefix.length();i++){
            char t = prefix.charAt(i);
            if(temp.list.get(t)!=null)temp = temp.list.get(t);
            else return false;
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */