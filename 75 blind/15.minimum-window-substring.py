class Solution:
    def minWnddow(self, s: str, t: str) -> str:
        # return self.first_solution(s, t)
        return self.second_solution(s, t)

    def first_solution(self, s: str, t: str) -> str:
        min_wnd = (float("infinity") , (-1, -1))
        l, r = 0, 0

        count_t = {}
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)

        count_wnd = {}
        
        while r < len(s):
            count_wnd[s[r]] = 1 + count_wnd.get(s[r], 0)
            # print(count_wnd)

            validWnd = self.isValidWnd(count_wnd, count_t)

            if not validWnd:
                r += 1
                continue
            
            while validWnd:
                if min_wnd[0] >= r - l + 1:
                    min_wnd = (r - l + 1, (r, l))

                count_wnd[s[l]] -= 1
                l += 1

                validWnd = self.isValidWnd(count_wnd, count_t)

            r += 1
        
        end, start = min_wnd[1]
        return s[start:end+1]

    def isValidWnd(self, count_wnd: dict, count_t: dict) -> bool:
        for c in count_t:
            if count_wnd.get(c, 0) < count_t[c]:
                return False

        return True
    
    def second_solution(self, s: str, t: str) -> str:
        minWnd = (float("infinity"), (-1, -1))

        count_t, count_wnd = {}, {}

        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)

        have, need = 0, len(count_t)

        l = 0
        for r in range(len(s)):
            c = s[r]

            if c in count_t:
                count_wnd[c] = 1 + count_wnd.get(c, 0)

                if count_wnd[c] == count_t[c]:
                    have += 1
                
            while have == need:
                if minWnd[0] > r - l + 1:
                    minWnd = (r - l + 1, (l, r))
                
                if s[l] in count_t:
                    count_wnd[s[l]] -= 1
                    if count_wnd[s[l]] < count_t[s[l]]:
                        have -= 1
                l += 1

        start, end = minWnd[1]
        return s[start : end + 1]




sol = Solution()
print("Sol:\n", sol.minWnddow("ADOBECODEBANC", "ABC"))