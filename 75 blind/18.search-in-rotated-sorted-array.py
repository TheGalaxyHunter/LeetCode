class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        while l <= r:
            if nums[l] < nums[r]:
                mid = (r + l) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                elif target < nums[mid]:
                    r = mid - 1
                else:
                    return -1
                continue
            
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid -1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1


        return -1
    

sol = Solution()
print(sol.search([4,5,6,7,0,1,2], 0), "should be 4")
print(sol.search([4,5,6,7,0,1,2], 3), "should be -1")
print(sol.search([1], 0), "should be -1")
print(sol.search([1,3], 0), "should be -1")
print(sol.search([1,3], 1), "should be 0")
print(sol.search([1,3], 3), "should be 1")
print(sol.search([3,1], 1), "should be 1")
print(sol.search([3,1], 3), "should be 0")
print(sol.search([4,5,6,7,8,1,2,3], 8), "should be 4")