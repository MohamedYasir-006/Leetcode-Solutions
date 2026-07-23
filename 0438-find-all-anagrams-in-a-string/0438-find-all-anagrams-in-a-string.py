class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res, need, window = [], Counter(p), Counter()
        l = len(p)
        for i, ch in enumerate(s):
            window[ch] += 1
            if i >= l: 
                window[s[i-l]] -= 1
                if window[s[i-l]] == 0: del window[s[i-l]]
            if window == need: res.append(i-l+1)
        return res

