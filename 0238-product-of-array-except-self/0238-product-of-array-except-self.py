class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*n
        suffix=1
        ans[0]=1
        
        for i in range(1,n):
            ans[i]=ans[i-1]*nums[i-1]
        for j in range(n-1,-1,-1):
            ans[j]=ans[j]*suffix
            suffix=suffix*nums[j]
        return ans

       