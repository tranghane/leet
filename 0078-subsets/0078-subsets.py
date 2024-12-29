class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curSubset = []

        def dfs (i):
            if i == len(nums):
                ans.append(curSubset.copy())
                return
            curSubset.append(nums[i])
            dfs(i+1)
            curSubset.pop()
            dfs(i+1)
        
        dfs(0)

        return ans
