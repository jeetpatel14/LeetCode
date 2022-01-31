class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=[True]*len(candies)
        for x in range(len(candies)):
            if candies[x]+extraCandies<max(candies):
                ans[x]=False
        return ans