from typing import List


def canPartition(nums: List[int]) -> bool:
    n = len(nums)
    if n < 2:
        return False

    total = sum(nums)
    maxNum = max(nums)
    if total & 1:
        return False

    target = total // 2
    if maxNum > target:
        return False

    dp = [[False] * (target + 1) for _ in range(n)]
    for i in range(n):
        dp[i][0] = True

    dp[0][nums[0]] = True
    for i in range(1, n):
        num = nums[i]
        for j in range(1, target + 1):
            dp[i][j] = dp[i - 1][j]
            if nums[i] <= j:
                dp[i][j] |= dp[i - 1][j - num]

    return dp[n - 1][target]


if __name__ == '__main__':
    canPartition([1, 5, 11, 5])
