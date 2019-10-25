class MyCircularQueue {
    int []q;
    int N=0;
    int front = -1;
    int rear = -1;
    /** Initialize your data structure here. Set the size of the queue to be k. */
    public MyCircularQueue(int k) {
        N=k;
        q= new int[k];
    }
    
    /** Insert an element into the circular queue. Return true if the operation is successful. */
    public boolean enQueue(int value) {
        if((rear+1)%N==front){
            return false;
        }
        else if(front == -1 && rear == -1){
            front=0;
            rear=0;
            q[rear]=value;
            return true;
        }
        else{
            rear=(rear+1)%N;
            q[rear]=value;
            return true;
        }
    }
    
    /** Delete an element from the circular queue. Return true if the operation is successful. */
    public boolean deQueue() {
        if(front==-1 && rear==-1){
            return false;
        }
        else if(front ==rear ){
            front=-1;
            rear=-1;
            return true;
        }
        else{
            front=(front+1)%N;
            return true;
        }
        
    }
    
    /** Get the front item from the queue. */
    public int Front() {
        if(front==-1&& rear==-1){
            return -1;
        }
        else{
            return q[front];
        }
        
    }
    
    /** Get the last item from the queue. */
    public int Rear() {
        if(front==-1 && rear == -1){
            return -1;
        }
        else{
            return q[rear];
        }
        
    }
    
    /** Checks whether the circular queue is empty or not. */
    public boolean isEmpty() {
        if(front==-1 && rear==-1){
            return true;
        }
        else{
            return false;
        }
    }
    
    /** Checks whether the circular queue is full or not. */
    public boolean isFull() {
        if((rear+1)%N==front){
            return true;
        }
        else{
            return false;
        }
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */