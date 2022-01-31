class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans =[first]
        for x in range(len(encoded)):
            ans.append(ans[x]^encoded[x])
        return ans