import random

from typing import List


def randomized_quick_sort(i, j, nums):
    pivot = random.randint(i, j)
    nums[pivot], nums[j] = nums[j], nums[pivot]
    idx = i - 1
    for k in range(i, j):
        if nums[k] < nums[j]:
            idx += 1
            nums[idx], nums[k] = nums[k], nums[idx]
    idx += 1
    nums[idx], nums[j] = nums[j], nums[idx]
    return idx


def randomized_quicksort(nums, l, r, k):
    if l > r:
        return nums[k]
    i = randomized_quick_sort(nums, l, r)
    if i == k:
        return nums[i]
    elif i < k:
        return randomized_quicksort(nums, i + 1, r, k)
    else:
        return randomized_quicksort(nums, l, i - 1, k)


def findKthLargest(nums: List[int], k: int) -> int:
    target = len(nums) - k
    return randomized_quicksort(nums, 0, len(nums) - 1, target)
