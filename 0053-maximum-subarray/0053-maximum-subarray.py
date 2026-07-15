class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        currentsum=0
        maximum=float('-inf')
        for i in range(len(nums)):
            currentsum+=nums[i]
            maximum=max(currentsum,maximum)

            if currentsum<0:
                currentsum=0

        return maximum
            