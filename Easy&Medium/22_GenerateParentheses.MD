<font face="微软雅黑">
This is a question worth considering.  
My thought process: Recursion(Backtracking) -> Recursion(Closure Number) -> Dynamic Planning  
Tip: For the recursion as well as DP, we first find the initial condition, and the recursive method from n-1 to n.</font>    
--------------------
**1.Recursion(Backtracking)**  
We only add '(' or ')' when it will remain a valid sequence.  
Time Complexity or Space Complexity : O(4^n/sqrt(n))    
```py
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        # 'left\right' as the counter of opening\closing brackets
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append(S)
                return
            # Condition1: #Opening brackets < N
            if left < n:
                backtrack(S + '(', left + 1, right)
            # Condition2: Whenever #Opening brackets > #Closing brackets
            if left > right:
                backtrack(S + ')', left, right + 1)
        
        backtrack()
        return ans
```
------------------------
**2.Recursion(Closure Number)**  
For each closure number c, we know the starting and ending brackets must be at index 0 and 2*c + 1.  
Then, the 2*c elements between must be a valid sequence, plus the rest of the elements must be a valid sequence.  
Time Complexity or Space Complexity : O(4^n/sqrt(n))   
```py
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        if n == 0:
            return ['']
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n-(c+1)):
                    ans.append('({}){}'.format(left, right))
        return ans
```
There is another similar method with less recursion.
But its time complexity is too hard to analyze.(滑稽)  
```py
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0: return ['']
        if n == 1: return ['()']
        ans = set()
        pre = self.generateParenthesis(n-1)
        for c in pre:
            for i in range(len(c)):
                ans.add(c[:i]+'()'+c[i:])
        ans = list(ans)
        return ans
```
------------------------  
**3.Dynamic Planning**  
Differently to Method2, we store ans[i] in DP-dict everytime we get ans[i], avoiding duplicate recursion.  
But it cause more space requirement. 
```py
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
		#initialization for dp in form of dic
        dp = {0: [''], 1: ['()'], 2: ['(())', '()()']}
        if n > 2:
            for i in range(3,n+1):
                temp = []
                for j in range(i):
                    for l in dp[j]:
                        for r in dp[i-j-1]:
                            temp.append('({}){}'.format(l, r))
                dp[i] = temp
        return dp[n]
```
