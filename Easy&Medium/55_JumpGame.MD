说明：前面三种方法都未通过
---------------------------------------
##1.Backtracking(回溯递归)  
时间复杂度：O(2^N)  
--证明  
![](https://github.com/yhcccc/MyLeetCode/raw/master/Easy&Medium/A.png)  
空间复杂度：O(N)
```py
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        return self.canJfinder(0, nums, n)
    
    def canJfinder(self, p, nums, n):
        
        if p == n - 1:
            return True
        
        pfurthest = min(p + nums[p], n - 1)
        for pnext in range(pfurthest, p, -1): #逆序遍历，大多数情况会更快的找到答案，除非极端情况
            if self.canJfinder(pnext, nums, n):
                return True
        
        return False
```
---------------------------------------
##2.Dynamic Programming Top-down(自顶向下) 
用一个表存储已访问的位置，避免了重复查询一些bad点
时间复杂度：O(N^2)  
空间复杂度：O(2N)=O(N)
```py
class Solution:
    
    Judgment = []
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        self.Judgment = [0]*(n - 1) + [1] #动态存储表初始化
        '''
        0--unknown
        1--good
        2--bad
        '''
        return self.canJfinder(0, nums, n)
    
    def canJfinder(self, p, nums, n):
        
        if self.Judgment[p] == 1:
            return True
        
        if self.Judgment[p] == 2:
            return False
        
        Jfurthest = min(p + nums[p], n - 1)
        for pnext in range(Jfurthest, p, -1):
            if self.canJfinder(pnext, nums, n):
                self.Judgment[p] = 1
                return True
        
        self.Judgment[p] = 2
        return False
```
---------------------------------------
##3.Dynamic Programming Bottom-up(自底向上) 
在前一方法的基础上消除了递归，是通过逆序遍历实现的
时间复杂度：O(N)  
空间复杂度：O(1)
```py
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        Judgment = [0]*(n - 1) + [1]
        
        for i in range(n - 2, -1, -1):
            Jfurthest = min(i + nums[i], n - 1)
            for j in range(i + 1, Jfurthest + 1):
                if Judgment[j] == 1:
                    Judgment[i] = 1
        
        return Judgment[0] == 1
```
---------------------------------------
##4.Greedy Algorithm
只记录一个left-most点--最左端的good点，
时间复杂度：O(N^2)  
空间复杂度：O(2N)=O(N)
```py
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        leftmost = n - 1
        for i in range(n - 2, -1, -1):
            if i + nums[i] >= leftmost: #key--判断是否更新left-most
                leftmost = i
                continue;
        return leftmost == 0
```
