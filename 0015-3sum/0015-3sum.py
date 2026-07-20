class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        result = []

        if n < 3:
            return []

        nums.sort()

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            n1 = nums[i]
            target = -n1

            j = i + 1
            k = n - 1

            while j < k:
                if nums[j] + nums[k] > target:
                    k -= 1

                elif nums[j] + nums[k] < target:
                    j += 1

                else:
                    result.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return result