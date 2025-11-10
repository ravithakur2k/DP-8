# Time complexity is: O(n^2) and space is also same O(m*n) because of self.memo and recursion depth

# The intuition is a simple DFS recursive approach where we have to check the next row first and second index and chose the minimum between the two.

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.memo = {}

        def helper(r, c):
            if r >= len(triangle):
                return 0
            if (r, c) in self.memo:
                return self.memo[(r, c)]
            case1 = helper(r + 1, c)
            case2 = helper(r + 1, c + 1)

            self.memo[(r, c)] = triangle[r][c] + min(case1, case2)
            return self.memo[(r, c)]

        return helper(0, 0)


#Bottom up solution, where we start from last row and calculate the dp array using similar logic to recursion. value plus minimum of the i and i + 1 index.
#Time O(n^2) and space is O(n)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * (len(triangle) + 1)
        for row in triangle[::-1]:
            for i, n in enumerate(row):
                dp[i] = n + min(dp[i], dp[i + 1])

        return dp[0]