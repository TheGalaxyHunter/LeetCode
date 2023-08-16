class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1

        max_area = 0

        while l < r:
            area = r-l
            if height[l] <= height[r]:
                area *= height[l]
                l += 1
            elif height[l] > height[r]:
                area *= height[r]
                r -= 1

            max_area = max(max_area, area)

        return max_area
    

sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]), "should be 49")
print(sol.maxArea([1,1]), "should be 1")
print(sol.maxArea([4,3,2,1,4]), "should be 16")
print(sol.maxArea([1,2,1]), "should be 2")