"""
一条包含字母 A-Z 的消息通过以下映射进行了 编码 ：

'A' -> 1
'B' -> 2
...
'Z' -> 26

要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，"11106" 可以映射为：

    "AAJF" ，将消息分组为 (1 1 10 6)
    "KJF" ，将消息分组为 (11 10 6)

注意，消息不能分组为  (1 11 06) ，因为 "06" 不能映射为 "F" ，这是由于 "6" 和 "06" 在映射中并不等价。

给你一个只含数字的 非空 字符串 s ，请计算并返回 解码 方法的 总数 。

题目数据保证答案肯定是一个 32 位 的整数。
"""


def numDecodings(s: str) -> int:
    len_ = len(s)
    dp = [[0 for _ in range(len_ + 1)] for _ in range(len_ + 1)]
    for i in range(len_):
        dp[i][i] = 1
    for i in range(len_):
        for j in range(i + 1, len_ + 1):
            if i + 1 == j:
                if s[i] != '0':
                    dp[i][j] = 1
            else:
                if s[j - 1] != '0':
                    dp[i][j] = max(dp[i][j], dp[i][j - 1])
                if j - i >= 2:
                    if s[j-2] != '0' and int(s[j - 2:j]) <= 26:
                        dp[i][j] += dp[i][j - 2]
    return dp[0][-1]


if __name__ == '__main__':
    numDecodings("06")
