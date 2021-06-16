from typing import List

"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
"""


def maxSubArray(nums: List[int]) -> int:
    prev = nums[0]
    for idx in range(1, len(nums)):
        if prev >= 0:
            prev += nums[idx]
        else:
            prev = nums[idx]
    return prev


if __name__ == '__main__':
    maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
