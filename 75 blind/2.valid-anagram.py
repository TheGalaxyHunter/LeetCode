class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return self.dict_sol(s, t)
        # return self.sort_sol(s, t)
        return self.array_sol(s, t)

    def sort_sol(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def dict_sol(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        c1 = {}
        c2 = {}

        for i in range(len(s)):
            c1[s[i]] = c1.get(s[i], 0) + 1
            c2[t[i]] = c2.get(t[i], 0) + 1

        return c1 == c2

    def array_sol(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26

        for i in range(len(s)):
            char1 = s[i]
            char2 = t[i]

            count[ord(char1) - ord('a')] += 1
            count[ord(char2) - ord('a')] -= 1

        # for x in count:
        #     if x != 0:
        #         return False

        # return True

        return count == [0] * 26
    
sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))
print(sol.isAnagram("rat", "car"))