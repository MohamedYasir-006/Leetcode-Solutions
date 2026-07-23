class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}

        # Count characters in magazine
        for ch in magazine:
            count[ch] = count.get(ch, 0) + 1

        # Use characters for ransomNote
        for ch in ransomNote:
            if count.get(ch, 0) == 0:
                return False
            count[ch] -= 1

        return True