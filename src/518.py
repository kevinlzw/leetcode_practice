from typing import List


def change(amount: int, coins: List[int]) -> int:
    dp = [0 for _ in range(amount + 1)]
    dp[0] = 1
    for coin in coins:
        for i in range(1, amount + 1):
            if i >= coin:
                dp[i] += dp[i - coin]
    return dp[-1]