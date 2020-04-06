class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashMap <Integer, Integer> h = new HashMap <Integer,Integer>();
        for(int i=0;i<nums.length;i++){
            if(h.containsKey(nums[i])){
                return true;
            }
            else{
                h.put(nums[i],nums[i]);
            }
        }
        return false;
    }
}