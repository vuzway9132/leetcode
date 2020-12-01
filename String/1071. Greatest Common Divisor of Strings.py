class Solution:
  def gcdOfStrings(self, str1: str, str2: str) -> str:
    candidate_len = math.gcd(len(str1), len(str2))
    candidate = str1[:candidate_len]
    if str1 + str2 == str2 + str1:
      return candidate
    return ''
