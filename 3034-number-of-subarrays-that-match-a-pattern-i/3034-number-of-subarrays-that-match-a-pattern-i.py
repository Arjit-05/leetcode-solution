class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n=len(nums)
        m=len(pattern)

        count=0

        for i in range(n-m):
            k=0
            while k<m:
                if pattern[k] == 1 and nums[i + k + 1] > nums[i + k]:
                    k+=1
                elif pattern[k] == 0 and nums[i + k + 1] == nums[i + k]:
                    k+=1
                elif pattern[k] == -1 and nums[i + k + 1] < nums[i + k]:
                    k+=1
                else:
                    break
                
            if k == m:
                count+=1
        return count  