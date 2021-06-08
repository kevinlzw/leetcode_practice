from typing import List


def findMaxForm(strs: List[str], m: int, n: int) -> int:
    old_dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for str_idx in range(len(strs)):
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        cnt_0 = strs[str_idx].count('0')
        cnt_1 = strs[str_idx].count('1')
        for i in range(n+1):
            for j in range(m+1):
                if j >= cnt_0 and i >= cnt_1:
                    dp[i][j] = max(old_dp[i - cnt_1][j - cnt_0] + 1, old_dp[i][j])
                else:
                    dp[i][j] = old_dp[i][j]
        old_dp = dp
    return old_dp[-1][-1]


if __name__ == '__main__':
    findMaxForm(["10", "0", "1"], 1, 1)
