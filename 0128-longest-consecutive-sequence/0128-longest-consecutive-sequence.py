class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_count=0
        new_set=set(nums)
        for num in new_set:
            if num -1 not in new_set:
                current=num
                count=1
                while current+1 in new_set:
                    count+=1
                    current+=1
                max_count=max(max_count,count)
        return max_count
        
