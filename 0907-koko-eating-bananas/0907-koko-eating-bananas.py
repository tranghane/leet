class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2

            sumBan = 0
            for i in piles:
                sumBan += ceil(i/mid)
            
            if (sumBan > h):
                left = mid + 1
            else:
                right = mid

        return right