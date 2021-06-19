from typing import List


def maxLength(arr: List[str]) -> int:
    masks = []
    for s in arr:
        mask = 0
        for c in s:
            idx = ord(c) - ord("a")
            if (1 << idx) & mask != 0:
                mask = 0
                break
            mask |= 1 << idx
        if mask > 0:
            masks.append(mask)

    ans = 0

    def back(idx, mask):
        if idx == len(masks):
            nonlocal ans
            ans = max(ans, bin(mask).count('1'))
            return
        if masks[idx] & mask == 0:
            back(idx + 1, masks[idx] | mask)
        back(idx+1, mask)

    back(0, 0)
    return ans