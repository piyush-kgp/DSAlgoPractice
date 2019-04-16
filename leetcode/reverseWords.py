# class Solution(object):
#     def reverseWords(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         words = []
#         start = 0
#         end = 0
#         # print(len(s), 'lenght')
#         for i in range(len(s)):
#             char = s[i]
#             # print(char, start, end)
#             if char == ' ':
#                 if end > start:
#                     words.append(s[start:end])
#                 start = end = i+1
#             else:
#                 end += 1
#         words.append(s[start:end])
#         # print(words)
#         rev_words = []
#         for i in range(len(words)):
#             if len(words[-1-i])>0:
#                 rev_words.append(words[-1-i])
#         # print(rev_words)
#         # return ' '.join(rev_words)
#         if len(rev_words) == 1:
#             return rev_words[0]
#         else:
#             return ' '.join(rev_words)

class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # just for the record the 1 line below does the job too
        return " ".join(x[::-1] for x in s.split(" "))
        t = []
        i = 0
        y = ""
        while i<len(s):
            j = i
            word = []
            while j< len(s) and s[j] != " ":
                word.append(s[j])
                j = j+1
            # print(word, i, j)
            x = ""
            for pos in range(j-1, i-1, -1):
                # print(s[pos])
                x = x+s[pos]
            y = y + x + " "
            i = j+1
        return y[:-1]
