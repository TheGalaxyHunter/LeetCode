class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = [[] for _ in range(len(nums)+1)]
        count_d = {}

        for i in nums:
            count_d[i] = 1 + count_d.get(i, 0)

        for num, count in count_d.items():
            freq[count].append(num)

        res = []
        for i in range(len(freq)-1, 0, -1):
            res += freq[i]

            if len(res) >= k:
                return res[:k]
        
            # for x in freq[i]:
            #     res.append(x)
            #     if len(res) == k:
            #         return res

        # O(n)


sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3], 2))
print(sol.topKFrequent([1], 1))
print(sol.topKFrequent([1,2], 2))
print(sol.topKFrequent([1,2,2], 2))
print(sol.topKFrequent([1,2,2,3,3,3], 2))
print(sol.topKFrequent([1,2,2,3,3,3,3], 2))
print(sol.topKFrequent([1,2,2,3,3,3,3,3], 2))