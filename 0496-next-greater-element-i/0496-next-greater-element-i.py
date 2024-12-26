class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        decreasingStack = [] #contain [num, index]

        for newNum in nums2:
            while decreasingStack and decreasingStack[-1] < newNum:
                topNum = decreasingStack.pop()
                dic[topNum] = newNum
            decreasingStack.append(newNum)
        
        for index, num in enumerate(nums1):
            if num in dic:
                nums1[index] = dic[num]
            else:
                 nums1[index] = -1
        return nums1
            


