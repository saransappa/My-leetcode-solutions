class Solution {
    public int maxSubArray(int[] nums) {
        return MSS(nums,0,nums.length-1);
    }
    
    public int max(int a,int b){
        if(a>b){return a;}
        else {return b;}
    }
    
    public int MSS(int [] nums,int low, int high){
        if(low == high){
            return nums[low];
        }
        int mid = (low+high)/2;
        int leftMSS = MSS(nums,low,mid);
        int rightMSS = MSS(nums,mid+1,high);
        
        int leftSum = Integer.MIN_VALUE;
        int rightSum = Integer.MIN_VALUE;
        
        int sum=0;
        for(int i=mid;i>=0;i--){
            sum+=nums[i];
            leftSum = max(sum,leftSum);
        }
        sum=0;
        for(int i=mid+1;i<=high;i++){
            sum+=nums[i];
            rightSum = max(sum,rightSum);
        }
        
        int ans = max(leftMSS,rightMSS);
        return max(ans,leftSum+rightSum);
    }
}