class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numsSet = set(nums)
        max_len = 0
        
        for i in nums:
            seq_len = 1
            if (i-1) not in numsSet:
                while (i+seq_len) in numsSet:
                    seq_len += 1
                max_len = max(max_len, seq_len)

        return max_len
    
sol = Solution()
print(sol.longestConsecutive([100,4,200,1,3,2]))
print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(sol.longestConsecutive([100, 102, 104]))