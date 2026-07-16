class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1

        index=0
        for color in [0,1,2]:
            if color in freq:
                for i in range(freq[color]):
                    nums[index]=color
                    index+=1
        return nums