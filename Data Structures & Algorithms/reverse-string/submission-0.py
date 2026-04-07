# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         res=[]
#         for i in s:
#             res.append(i)
#         res.reverse()
#         return res

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
        return s