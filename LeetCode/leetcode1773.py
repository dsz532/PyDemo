class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        ans = 0
        for i in items:
            if ruleKey == 'type':
                if i[0] == ruleValue:
                    ans += 1
            elif ruleKey == 'color':
                if i[1] == ruleValue:
                    ans += 1
            elif ruleKey == 'name':
                if i[2] == ruleValue:
                    ans += 1
        return ans


pass

solutuon = Solution()
items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"
print(solutuon.countMatches(items, ruleKey, ruleValue))
