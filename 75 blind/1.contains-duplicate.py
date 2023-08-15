class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # return self.hset_solution(nums)
        return self.sort_solution(nums)

    def hset_solution(self, nums: list[int]) -> bool:
        hset = set()

        for i in nums:
            if i in hset:
                return True
            else:
                hset.add(i)

        return False
    
    def sort_solution(self, nums: list[int]) -> bool:
        nums = sorted(nums)

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        
        return False
    
sol  = Solution()
print(sol.containsDuplicate([1,2,3,1]))