class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        L = len(s)
        ok = [True]
        breaks = [0]
        words = []
        for i in range(1, L+1):
            ok.append(any(ok[j] and s[j:i] in wordDict for j in range(i)))
            if any(ok[j] and s[j:i] in wordDict for j in range(i)):
                words.append(s[breaks[-1]:i])
                breaks.append(i)
        print(breaks, words, ok)
        return ok[-1]
