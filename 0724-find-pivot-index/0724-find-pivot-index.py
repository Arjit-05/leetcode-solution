class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        
        TotalSum=0
        for sum in nums:
            TotalSum+=sum
        
        prefix=[0]*n
        prefix[0]=nums[0]
        for j in range(1,n):
            prefix[j]=prefix[j-1] + nums[j]

        for i in range(n):
            if i == 0:
                ls=0
            else:
                ls=prefix[i-1]
            rs=TotalSum - ls - nums[i]

            if ls == rs:
                return i
        return -1
