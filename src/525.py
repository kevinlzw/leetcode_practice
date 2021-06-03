from collections import defaultdict
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        counter = 0
        cnt_qianzhui = defaultdict(int)
        cnt_qianzhui[0] = -1
        max_ = 0
        for idx in range(len(nums)):
            if nums[idx] == 1:
                counter += 1
            else:
                counter -= 1
            if counter not in cnt_qianzhui:
                cnt_qianzhui[counter] = idx
            else:
                max_ = max(idx - cnt_qianzhui[counter], max_)
        return max_


if __name__ == '__main__':
    a = Solution()
    a.findMaxLength([0, 1])
