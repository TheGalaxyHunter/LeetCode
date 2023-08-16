class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1

        while i < j:

            if not self.alnum(s[i]):
                i += 1
                continue
            if not self.alnum(s[j]):
                j -= 1
                continue

            if s[i].lower() != s[j].lower():
                print(s[i], s[j])
                return False
            
            i += 1
            j -= 1

        return True

    def alnum(self, c):
        return (ord('0') <= ord(c) <= ord('9') or
                ord('a') <= ord(c) <= ord('z') or
                ord('A') <= ord(c) <= ord('Z'))
            