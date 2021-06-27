from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        res = []
        def retrieve(idx, str_):
            if idx == len(s):
                res.append("".join(str_))
            else:
                for i in range(idx, len(s)):
                    str_[i], str_[idx] = str_[idx], str_[i]
                    retrieve(idx+1, str_)
                    str_[idx], str_[i] = str_[i], str_[idx]
        retrieve(0, list(s))
        return res

if __name__ == '__main__':
    a = Solution()
    a.permutation("abc")