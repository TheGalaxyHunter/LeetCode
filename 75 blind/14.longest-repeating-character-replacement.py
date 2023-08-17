class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_size = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            max_size = max(max_size, r - l + 1)

        return max_size
    
sol = Solution()
print(sol.characterReplacement("ABAB", 2))
print(sol.characterReplacement("AABABBA", 2))
print(sol.characterReplacement("AABABBA", 0))