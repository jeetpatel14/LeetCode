class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        int numsSize=nums.size();
    vector<int> ans;
    for(int i=0;i<numsSize;i++)
    {
        int a = 0;
        for(int j=0;j<numsSize;j++)
        {
            if(nums[i]>nums[j] && i!=j)
                a++;
        }
        ans.push_back(a);
    }
    return ans;
    }
};