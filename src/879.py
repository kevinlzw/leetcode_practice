from typing import List


def profitableSchemes(n, minProfit, group, profit):
    dp = [[[0 for _ in range(minProfit+1)] for _ in range(n + 1)] for _ in range(len(group) + 1)]
    dp[0][0][0] = 1
    for idx_group in range(1, len(group)+1):
        group_mem, earn_profit = group[idx_group-1], profit[idx_group-1]
        for idx_employee in range(n + 1):
            for profit_idx in range(minProfit+1):
                if idx_employee < group_mem:
                    dp[idx_group][idx_employee][profit_idx] = dp[idx_group - 1][idx_employee][profit_idx]
                else:
                    dp[idx_group][idx_employee][profit_idx] = dp[idx_group - 1][idx_employee][profit_idx] + \
                                                          dp[idx_group - 1][idx_employee - group_mem][
                                                              max(0, profit_idx - earn_profit)]
    total = sum(dp[len(group)][j][minProfit] for j in range(n + 1))
    return total % (10 ** 9 + 7)


if __name__ == '__main__':
    profitableSchemes(5, 3, [2, 2], [2, 3])
