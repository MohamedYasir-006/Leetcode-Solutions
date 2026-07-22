class Solution:
    def canJump(self, nums: List[int]) -> bool:
        a = 0

        for i in range(len(nums)):
            if i > a:
                return False

            a = max(a, i + nums[i])

            if a >= len(nums) - 1:
                return True

        return True