class Node{
    int data;
    Node next;
}
class MyLinkedList {
    Node head = null;
    /** Initialize your data structure here. */
    public MyLinkedList() {
        
    }
    
    /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    public int get(int index) {
        int j=0;
        Node t =head;
        while(t!=null){
            t=t.next;
            j++;
        }
        
        if(index < j && index >=0){
            Node temp =head;
            int i = 0;
            while(i<index){
                temp=temp.next;
                i++;
            }
            return temp.data;
        }
        return -1;
    }
    
    /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
    public void addAtHead(int val) {
        Node newnode = new Node();
        newnode.data = val;
        newnode.next = head;
        head = newnode;
    }
    
    /** Append a node of value val to the last element of the linked list. */
    public void addAtTail(int val) {
        Node temp = head;
        while(temp.next!=null){
            temp = temp.next;
        }
        Node newnode =  new Node();
        newnode.data = val;
        temp.next = newnode;
        newnode.next = null;
    }
    
    /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
    public void addAtIndex(int index, int val) {
        int j=0;
        Node t =head;
        while(t!=null){
            t=t.next;
            j++;
        }
        if(index<=j && index>0){
            int i=0;
            Node temp = head;
            while(i<index-1){
                temp = temp.next;
                i++;
            }
            Node newnode = new Node();
            newnode.data = val;
            newnode.next = temp.next;
            temp.next = newnode;
        }
        else if(index<=0){
            Node newnode = new Node();
            newnode.data = val;
            newnode.next = head;
            head = newnode;
        }
    }
    /** Delete the index-th node in the linked list, if the index is valid. */
    public void deleteAtIndex(int index) {
        if(index==0){
            head=head.next;
        }
        else if(index>0){
            int j=0;
            Node t =head;
            while(t!=null){
                t=t.next;
                j++;
            }
            if(index<j){
                int i=0;
                Node temp = head;
                while(i<index-1){
                    temp = temp.next;
                    i++;
                }
                temp.next = temp.next.next;
            }
        }
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */