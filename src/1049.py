from typing import List


def lastStoneWeightII(stones: List[int]) -> int:
    n = len(stones)
    sum_ = sum(stones)
    intermediate = sum_ // 2

    dp = [[False for _ in range(intermediate + 1)] for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(1, n + 1):
        for j in range(intermediate + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= stones[i - 1]:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - stones[i - 1]]

    for i in range(intermediate, -1, -1):
        if dp[n][i]:
            ans = sum_ - 2 * i
            break
    return ans


if __name__ == '__main__':
    lastStoneWeightII([2, 7, 4, 1, 8, 1])
