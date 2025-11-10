# Time: O(n) and space is O(1)

# The intuition is create a dp array and if the difference between two consecutive elements is equal then we can add 1 to the previous result.
# Else the difference is not same then we have set the result to 0 basically starting to search for new arithmetic slice

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        curr = 0
        result = 0
        for i in range(2, n):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                curr = curr + 1
            else:
                curr = 0
            result += curr
        return result
