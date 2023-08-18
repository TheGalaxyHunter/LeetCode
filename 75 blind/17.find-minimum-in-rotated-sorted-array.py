class Solution:
    def findMin(self, nums: list[int]) -> int:
        min_val = nums[0]
        l, r = 0, len(nums)-1

        while l <= r:
            if nums[l] < nums[r]:
                min_val = min(min_val, nums[l])
                break

            mid = (l + r) // 2
            min_val = min(min_val, nums[mid])

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        
        return min_val
    
sol = Solution()
print(sol.findMin([3,4,5,1,2]))
print(sol.findMin([4,5,6,7,0,1,2]))
print(sol.findMin([11,13,15,17]))