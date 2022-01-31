class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        ans=[]
        for i in range(len(nums)):
            hashtable[nums[i]]=i
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hashtable:
                if i!=hashtable[difference]:
                    ans.append(i)
                    ans.append(hashtable[difference])
                    break
        return ans