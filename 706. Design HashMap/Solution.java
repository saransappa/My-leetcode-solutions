class HashNode{
    int key;
    int value;
    HashNode(int k,int v){
        key = k;
        value = v;
    }
}


class MyHashMap {
    int size = 1000000;
    HashNode [] harr;
    
    public int hash(int k){
        return k%size;
    }
    
    /** Initialize your data structure here. */
    public MyHashMap() {
         harr  = new HashNode[size];
    }
    
    /** value will always be non-negative. */
    public void put(int key, int value) {
        int ind = hash(key);
        if(harr[ind]==null){
            harr[ind] = new HashNode(key,value);
        }
        else{
            harr[ind].value = value;
        }
    }
    
    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    public int get(int key) {
        int ind = hash(key);
        if(harr[ind]!=null){
            HashNode h = harr[ind];
            return h.value;
        }
        return -1;
    }
    
    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    public void remove(int key) {
        int ind = hash(key);
        harr[ind] = null;
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */