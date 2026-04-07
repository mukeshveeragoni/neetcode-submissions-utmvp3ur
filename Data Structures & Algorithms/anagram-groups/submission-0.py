class Solution:
    def groupAnagrams(self, str: List[str]) -> List[List[str]]:
        res={}
        for word in str:
            key="".join(sorted(word))
            if key not in res:
                res[key]=[]
            res[key].append(word)
        return list(res.values())
        