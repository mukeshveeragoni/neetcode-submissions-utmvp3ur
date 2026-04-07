class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=nums[0]
        cur_sum=0
        for i in nums:
            if cur_sum<0:
                cur_sum=0
            cur_sum=cur_sum+i
            res=max(res,cur_sum)
        return res