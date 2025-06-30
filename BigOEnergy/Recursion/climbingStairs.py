"""
You are given an integer n representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.

Return the number of distinct ways to climb to the top of the staircase.

"""
class recursionSolution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n  # base case is 1 way to climb 1 step, 2 ways to climb 2 steps
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# memo and recursion
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dfs(steps):
        
            if steps <= 2:
                return steps

            if steps in memo:
                return memo[steps]
            memo[steps] = dfs(steps - 1) + dfs(steps - 2)
            return memo[steps]
        return dfs(n)


#
class OptimalSolution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        one, two = 1, 2

        for _ in range(3, n+1):
            one, two = two, one + two

        return two

# Time complexity of O(n) and Space of O(1)