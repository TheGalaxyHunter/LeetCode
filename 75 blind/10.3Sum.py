class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        for i, x in enumerate(nums):
            if i > 0 and nums[i-1] == x:
                continue
            
            l = i+1
            r = len(nums)-1
            while l < r:
                sum3 = nums[l] + nums[r] + x
                if sum3 == 0:
                    res.append([x, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif sum3 < 0:
                    l += 1
                elif sum3 > 0:
                    r -= 1

        return res
    
sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))
print(sol.threeSum([]))
print(sol.threeSum([0]))
print(sol.threeSum([0,0,0,0]))
