class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #dynamische programming
        for i in range(1, len(nums)):
            nums[i] += max( 0, nums[i-1])
        return max(nums)
