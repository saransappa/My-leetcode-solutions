class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        for(int i=0;i<nums2.size();i++){
            nums1.push_back(nums2.at(i));
        }
        sort(nums1.begin(),nums1.end());
        int length = nums1.size();
        if(length%2!=0){
            return nums1.at(length/2);
        }
        else{
            return ((double)nums1.at(length/2)+(double)nums1.at(length/2 -1))/2.0;
        }
    }
};