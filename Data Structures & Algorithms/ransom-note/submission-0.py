class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        available = {}

        for char in magazine:
            available[char] = available.get(char,0) +1

        for char in ransomNote:
            if available.get(char,0) == 0:
                return False
            available[char] -= 1
        return True

             