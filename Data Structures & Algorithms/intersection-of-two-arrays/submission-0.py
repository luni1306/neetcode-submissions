class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = {}
        for s in nums1:
            seen[s] = seen.get(s,0) + 1
        
        result = []
        for t in nums2:
            if seen.get(t,0) > 0:
                result.append(t)
                seen[t] = 0
        return result
