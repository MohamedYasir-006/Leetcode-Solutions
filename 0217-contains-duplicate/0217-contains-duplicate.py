class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = set()
        for n in nums:
            if n in a:
                return True
            a.add(n)
        return False
