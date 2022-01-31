class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size = len(nums)
        i=0
        while i<size:
            nums.append(nums[i])
            i+=1
        return nums