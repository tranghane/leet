class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = 0
        for i in range(k):
            ans += nums[i]
        cur_sum = ans

        for r in range(k, len(nums)):
            cur_sum += nums[r]
            cur_sum -= nums[r - k]

            ans = max(ans, cur_sum)
        
        return ans/k