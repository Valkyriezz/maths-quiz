class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        l=0
        r=n-1
        find=-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                find=mid
                break
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        if find==-1:
            return [-1,-1]
        #expand l and r from mid
        l=find
        r=find
        while l>0 and nums[l-1]==target:
            l-=1
        while r<n-1 and nums[r+1]==target:
            r+=1
        return [l,r]