class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxwater=0
        left=0
        right=len(height)-1

        while left <right:
            wt=right-left
            ht=min(height[left],height[right])
            curr_water=wt * ht
            maxwater=max(curr_water,maxwater)

            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxwater
