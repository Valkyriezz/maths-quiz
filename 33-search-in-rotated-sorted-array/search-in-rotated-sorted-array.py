class Solution:
    def search(self, nums: List[int], k: int) -> int:
        n=len(nums)
        l=0
        r=n-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==k:
                return mid
            if nums[l]<=nums[mid]:
                if nums[l]<=k<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if nums[mid]<=k<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
        return -1

            
