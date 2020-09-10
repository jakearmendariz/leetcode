class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr, best = 0, nums[0]
        
        for i in nums:
            curr += i
            best = max(curr, best)
            if curr < 0: curr = 0
        return best