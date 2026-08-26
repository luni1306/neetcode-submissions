class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i = 0
        s = {}
        for n in nums:
            if n in s:
                return True
            else:
                s[n] = i
                i += 1
        return False
                

        