class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def f(nums):
            prev1=0
            prev2=0
            for i in range(len(nums)):
                curr=max(nums[i]+prev2,prev1)
                prev2=prev1
                prev1=curr
            return prev1
        case1=f(nums[:-1])
        case2=f(nums[1:])
        return max(case1,case2)
        