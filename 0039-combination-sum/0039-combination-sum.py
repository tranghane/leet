class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        curList = []

        if not candidates:
            return []

        def dfs(i, curSum):
            if (curSum == target):
                ans.append(curList.copy())
                return
            if i == len(candidates) or curSum > target:
                return
            
            dfs(i+1, curSum)
            
            curList.append(candidates[i])
            dfs(i, curSum + candidates[i])
            curList.pop()
                

        dfs(0, 0)
        return ans
