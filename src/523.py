from collections import defaultdict

from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        qianzhui_sum = defaultdict(int)
        cur_sum = 0
        for idx, num in enumerate(nums):
            cur_sum += num
            yu = cur_sum % k
            if yu not in qianzhui_sum:
                qianzhui_sum[yu] = idx
            else:
                if idx - qianzhui_sum[yu] >= 2:
                    return True
        return False


if __name__ == '__main__':
    a = Solution()
    a.checkSubarraySum([23, 2, 4, 6, 6], 7)
