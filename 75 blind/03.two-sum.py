class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # return self.brute_sol(nums, target)
        return self.hashset_sol(nums, target)
        

    def brute_sol(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            k = target - nums[i]
            for j in range(i+1, len(nums)):
                if k == nums[j]:
                    return [i, j]

    def hashset_sol(self, nums: list[int], target: int) -> list[int]:
        dict_set = {nums[0]: 0}

        for i in range(1, len(nums)):
            k = target - nums[i]
            if k in dict_set:
                return [dict_set[k], i]
            dict_set[nums[i]] = i

sol = Solution()
print(sol.twoSum([2,7,11,15], 9))
print(sol.twoSum([3,2,4], 6))
print(sol.twoSum([3,3], 6))
