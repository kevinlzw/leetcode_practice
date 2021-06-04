from collections import Counter
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        cnt = Counter()
        res = set()
        for i in range(0, len(s) - 9):
            cnt[s[i:i + 10]] += 1
            if cnt[s[i:i + 10]] > 1:
                res.add(s[i:i + 10])
        return list(res)
