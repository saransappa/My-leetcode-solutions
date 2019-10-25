import java.util.*;
class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue <Integer> pQueue = new PriorityQueue <Integer> ();
        for(int i=0;i<nums.length;i++){
            pQueue.add(nums[i]);
        }
        int j=0;
        for(int i=0;i<=nums.length-k;i++){
            j=pQueue.poll();
        }
        return j;
    }
}