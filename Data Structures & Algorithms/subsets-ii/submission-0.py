class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        sol=[]
        nums.sort()
        def helper(index):
            res.append(sol[:])
            for i in range(index,len(nums)):
                if i > index and nums[i]==nums[i-1]:
                    continue
                sol.append(nums[i])
                helper(i+1)
                sol.pop()
        helper(0)
        return res