class Solution {
    public int maxProfit(int[] prices) {
        if(prices.length==0){
            return 0;
        }
        int [] nums = new int[prices.length-1];
        int c=0;
        for(int i=0;i<nums.length;i++){
            nums[i]=prices[i+1]-prices[i];
            if(nums[i]<0){c++;}
            //System.out.println(nums[i]);
        }
        if(c==nums.length){
            return 0;
        }
        return MSS(nums,0,nums.length-1);
    }
    public int max(int a,int b){
        if(a>b){return a;}
        else{return b;}
    }
    
    public int MSS(int [] nums,int low,int high){
        if(low==high){
            return nums[low];
        }
        
        int mid = (low+high)/2;
        int leftMSS = MSS(nums,low,mid);
        int rightMSS = MSS(nums,mid+1,high);
        int leftSum = Integer.MIN_VALUE;
        int rightSum = Integer.MIN_VALUE;
        int sum = 0;
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