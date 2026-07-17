class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        given=0
        for i in range(n+1):
            ans+=i
        for j in nums:
            given+=j
        ans=ans-given

        return ans
           