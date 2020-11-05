class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        if n < m*k:
            return False
        for l in range(n - m*k + 1):
            offset = 0
            while offset < m*k:
                if arr[l+offset] != arr[l+offset%m]:
                    break
                offset += 1
            if offset == m * k:
                return True
        return False
