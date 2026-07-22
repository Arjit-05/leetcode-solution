class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        maximum=max(nums)
        max_idx=nums.index(maximum)
        second_max=0
        for i in range(len(nums)):
            if i !=max_idx:
                if nums[i]>second_max:
                    second_max=nums[i]

        if maximum >= 2*second_max:
            return max_idx
        return -1

        

