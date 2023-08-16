class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        return self.first_sol(nums)
        # return self.second_sol(nums)

    def first_sol(self, nums: list[int]) -> list[int]:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        res = [0] * len(nums)

        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i]
        
        postfix[len(nums)-1] = nums[len(nums)-1]
        for i in range(len(nums)-2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i]

        for i in range(1, len(nums)-1):
            res[i] = prefix[i-1]*postfix[i+1]

        res[0] = postfix[1]
        res[len(nums)-1] = prefix[len(nums)-2]

        return res

    def second_sol(self, nums: list[int]) -> list[int]:
        res = [0] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i] 

        # print(res)

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
    
sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))
print(sol.productExceptSelf([-1,1,0,-3,3]))
print(sol.productExceptSelf([1,2,3,4,5,6,7,8,9,10]))
print(sol.productExceptSelf([1,2,3,4,5,6,7,8,9,10,11]))