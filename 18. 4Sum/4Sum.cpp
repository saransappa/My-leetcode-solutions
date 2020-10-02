class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(),nums.end());
        bool found = false;
        int n = nums.size();
        int k=0,l=n-1;
        vector<vector<int>>v;
        set<vector<int>> s;
        for(int k=0;k<n-1;k++){
            for(int l=1;l<n;l++){
                int i =0,j=n-1;
                int max_sum = INT_MIN;
                while(i<j){
                    int sum=0;
                    //cout<<nums[i]<<" "<<nums[j]<<" "<<nums[k]<<" "<<nums[l]<<endl;
                    if(k<l && i<j ){
                        set<int>sind;
                        sum = nums[i]+nums[j]+nums[k]+nums[l];
                        if(sum>max_sum)max_sum=sum;
                        if(sum==target){
                            //cout<<1<<endl;
                            found = true;
                            //cout<<nums[i]<<" "<<nums[j]<<" "<<nums[k]<<" "<<nums[l]<<endl;
                            sind.insert(i);
                            sind.insert(j);
                            sind.insert(k);
                            sind.insert(l);
                            if(sind.size()==4){
                                vector <int> temp={nums[i],nums[j],nums[k],nums[l]};
                                sort(temp.begin(),temp.end());
                                s.insert(temp);
                            }
                        }
                    }
                    if(sum>target)j--;
                    else i++;
                }
            }
        }
        //if(!found)cout<<0<<endl;
        //cout<<s.size()<<endl;
        for(auto it=s.begin();it!=s.end();it++){
            v.push_back((*it));
        }
        return v;
    }
};