"""
1. Clarification
2. Possible solutions
     - Brute Force
     - Recursion with Memoization
     - 2D Dynamic Programming
     - 1D Dynamic Programming
3. Coding
4. Tests
"""


# # T=O(2^n), S=O(n), Time Limit Exceeded
# class Solution:
#     def findTargetSumWays(self, nums: List[int], S: int) -> int:
#         if not nums: return 0
#         self.count = 0
#         self.calculate(nums, 0, 0, S)
#         return self.count
#
#     def calculate(self, nums, i, tmpSum, S):
#         if i == len(nums):
#             if tmpSum == S:
#                 self.count += 1
#         else:
#             self.calculate(nums, i + 1, tmpSum + nums[i], S)
#             self.calculate(nums, i + 1, tmpSum - nums[i], S)


# # T=O(ln), S=O(ln), l refers to the range of tmpSum
# class Solution:
#     def findTargetSumWays(self, nums: List[int], S: int) -> int:
#         if not nums: return 0
#         self.memo = {i: dict() for i in range(len(nums))}
#         self.count = 0
#         return self.calculate(nums, 0, 0, S)
# 
#     def calculate(self, nums, i, tmpSum, S):
#         if i == len(nums):
#             return 1 if tmpSum == S else 0
#         else:
#             if tmpSum in self.memo[i]:
#                 return self.memo[i][tmpSum]
#             add = self.calculate(nums, i + 1, tmpSum + nums[i], S)
#             sub = self.calculate(nums, i + 1, tmpSum - nums[i], S)
#             self.memo[i][tmpSum] = add + sub
#             return self.memo[i][tmpSum]


# T=O(ln), S=O(ln)
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums: return 0
        n = len(nums)
        dp = [[0] * 2001 for _ in range(n)]
        dp[0][nums[0] + 1000] = 1
        dp[0][-nums[0] + 1000] += 1
        for i in range(1, n):
            for tmpSum in range(-1000, 1001):
                if dp[i - 1][tmpSum + 1000] > 0:
                    dp[i][tmpSum + nums[i] + 1000] += dp[i - 1][tmpSum + 1000]
                    dp[i][tmpSum - nums[i] + 1000] += dp[i - 1][tmpSum + 1000]
        return 0 if S > 1000 else dp[n - 1][S + 1000]


# # T=O(ln), S=O(n)
# class Solution:
#     def findTargetSumWays(self, nums: List[int], S: int) -> int:
#         if not nums: return 0
#         dp = [0] * 2001
#         dp[nums[0] + 1000] = 1
#         dp[-nums[0] + 1000] += 1
#         for i in range(1, len(nums)):
#             next = [0] * 2001
#             for tmpSum in range(-1000, 1001):
#                 if dp[tmpSum + 1000] > 0:
#                     next[tmpSum + nums[i] + 1000] += dp[tmpSum + 1000]
#                     next[tmpSum - nums[i] + 1000] += dp[tmpSum + 1000]
#             dp = next
#         return 0 if S > 1000 else dp[S + 1000]