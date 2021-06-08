from typing import List


def findTargetSumWays(nums: List[int], target: int) -> int:
    sum_ = sum(nums)
    intermediate = sum_ + target
    if intermediate % 2 == 1:
        return 0
    pos = intermediate // 2
    dp = [[0 for _ in range(pos + 1)] for _ in range(len(nums) + 1)]
    dp[0][0] = 1
    for i in range(1, len(nums) + 1):
        for j in range(pos + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= nums[i-1]:
                dp[i][j] += dp[i - 1][j - nums[i-1]]
    return dp[-1][-1]


if __name__ == '__main__':
    findTargetSumWays([1, 1, 1, 1, 1], 3)
