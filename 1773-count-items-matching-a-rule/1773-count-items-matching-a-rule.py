class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey=="type":
            temp=0
        elif ruleKey=="color":
            temp=1
        else:
            temp=2
        count = 0
        for x in items:
            if x[temp]==ruleValue:
                count+=1
        return count