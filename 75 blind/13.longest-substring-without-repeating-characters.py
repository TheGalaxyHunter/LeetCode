class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c_set = set()
        max_len = 0
        l = 0
        
        for r in range(len(s)):
            while s[r] in c_set:
                c_set.remove(s[l])
                l += 1
            
            c_set.add(s[r])
            max_len = max(max_len, r - l + 1)    
               

        return max_len

sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
print(sol.lengthOfLongestSubstring("bbbbb"))
print(sol.lengthOfLongestSubstring("pwwkew"))