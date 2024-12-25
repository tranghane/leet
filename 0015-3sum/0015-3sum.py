class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        finalAns = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            if (nums[i] > 0):
                return finalAns
            target = -nums[i]
            low = i + 1
            high = len(nums) - 1
            while low < high:
                summ = nums[low] + nums[high]
                if (summ == target):
                    finalAns.append([-target, nums[high], nums[low]])
                    low, high = low+1, high-1
                    while (low < high and nums[low -1] == nums[low]):
                        low += 1
                    while (low < high and nums[high +1] == nums[high]):
                        high -= 1
                elif (summ > target):
                    high -= 1

                else:
                    low += 1

        return finalAns        


