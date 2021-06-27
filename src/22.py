from typing import List


# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def recur(tmp, left, right):
            if left == 0 and right == 0:
                res.append(tmp)
            else:
                if right < left:
                    return
                if left > 0:
                    recur(tmp + "(", left - 1, right)
                if right > 0:
                    recur(tmp + ")", left, right - 1)
        recur("", n, n)
        return res
