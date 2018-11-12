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
