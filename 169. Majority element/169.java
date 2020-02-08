class Solution {
    public int majorityElement(int[] nums) {
        return majorityRec(nums,0,nums.length-1);
    }
    
    public int majorityRec(int [] nums,int low,int high){
        if(low == high){
            return nums[low];
        }
        
        int mid = (low+high)/2;
        int leftMajor = majorityRec(nums,low,mid);
        int rightMajor = majorityRec(nums,mid+1,high);
        
        if(leftMajor == rightMajor){
            return leftMajor;
        }
        
        int leftCount = countRange(nums,leftMajor,low,high);
        int rightCount = countRange(nums,rightMajor,low,high);
        
        if(leftCount>rightCount){
            return leftMajor;
        }
        else{
            return rightMajor;
        }
    }
    
    public int countRange(int [] nums,int num,int i,int j){
        int count=0;
        for(int k=i;k<=j;k++){
            if(nums[k]==num){count++;}
        }
        return count;
    }
    
}