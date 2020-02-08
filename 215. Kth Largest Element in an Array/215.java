class Solution {
    public int findKthLargest(int[] nums, int k) {
        sort(nums,0,nums.length-1);
        return nums[k-1];
    }
    
    public void sort(int [] arr, int l,int r){
        if(l<r){
            int mid = (l+r)/2;
            sort(arr,l,mid);
            sort(arr,mid+1,r);
            
            merge(arr,l,mid,r);
        }   
        return;
    }
    
    public void merge(int [] arr,int l,int m,int r){
        int n1 = m-l+1;
        int n2 = r-m;
        
        int [] L = new int[n1];
        int [] R = new int[n2];
        int k=l;
        for(int i=0;i<n1;i++){
            L[i] = arr[k];
            k++;
        }
        for(int i=0;i<n2;i++){
            R[i] = arr[k];
            k++;
        }
        
        k=l;
        int i=0,j=0;
        while(i<n1 && j<n2){
            if(L[i]>R[j]){
                arr[k]=L[i];
                i++;
            }
            else{
                arr[k]=R[j];
                j++;
            }
            k++;
        }
        while(i<n1){
            arr[k]=L[i];
            i++;
            k++;
        }
        while(j<n2){
            arr[k]=R[j];
            j++;
            k++;
        }
    }
}