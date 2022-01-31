class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        freq,val,i=[],[],0
        ans=[]
        while i<len(nums):
            freq.append(nums[i])
            val.append(nums[i+1])
            i+=2
        for x in range(len(freq)):
            for y in range(freq[x]):
                ans.append(val[x])
        return ans