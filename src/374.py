# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        def binary_search(i, j):
            mid = (i + j) // 2
            res = guess(mid)
            if res == 0:
                return mid
            if res == -1:
                return binary_search(i, mid-1)
            if res == 1:
                return binary_search(mid+1, j)
        return binary_search(1, n)