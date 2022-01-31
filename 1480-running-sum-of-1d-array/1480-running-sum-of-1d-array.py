class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s,ans = 0,[]
        for i in nums:
            s+=i
            ans.append(s)
        return ans