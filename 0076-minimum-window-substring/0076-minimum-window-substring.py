class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1

        window = {}
        matched = 0

        left = 0
        min_len = float('inf')
        start = 0

        for right in range(len(s)):
            if s[right] in need:
                window[s[right]] = window.get(s[right], 0) + 1

                if window[s[right]] == need[s[right]]:
                    matched += 1

            while matched == len(need):

                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                if s[left] in need:
                    window[s[left]] -= 1

                    if window[s[left]] < need[s[left]]:
                        matched -= 1

                left += 1

        if min_len == float('inf'):
            return ""

        return s[start:start + min_len]


        