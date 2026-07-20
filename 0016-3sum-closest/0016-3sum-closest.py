class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closestSum=float('inf')
        n=len(nums)
        nums.sort()
        for k in range(n-2):
            i=k+1
            j=n-1
            while i<j:
                sum=nums[k] + nums[i] + nums[j]
                if abs(target-sum)< abs(target-closestSum):
                    closestSum=sum
                
                if sum<target:
                    i+=1
                else:
                    j-=1
        return closestSum


