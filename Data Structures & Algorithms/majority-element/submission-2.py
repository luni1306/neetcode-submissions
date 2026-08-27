class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = {}
        for s in nums:
            count[s] = count.get(s,0) + 1
        for n in count:
            if count[n] > len(nums)/2:
                return n
        