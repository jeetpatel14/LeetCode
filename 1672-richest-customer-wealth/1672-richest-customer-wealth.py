class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        for x in range(len(accounts)):
            accounts[x]=sum(accounts[x])
        return max(accounts)