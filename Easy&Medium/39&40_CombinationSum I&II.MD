------------------------------
**1.BFS(Breadth-First-Search) for I**  
Replace the recursion with a stack
```py
class Solution:
    def combinationSum(self, candidates, target):
        result = []
        stack = [(0, 0, [])]
        candidates.sort()
        while stack:
            start, counter, temp = stack.pop()
            if target == counter:
                result.append(temp[:])
                continue
            for i in range(start, len(candidates)):
                c = counter + candidates[i]
                if c > target: break
                else:
                    stack.append((i, c, temp + [candidates[i]]))
        return result
```
--------------------------------------------
**2.DFS(Depth-First-Search) for I&II**  
See <https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)>  
I optimized the algorithm with the idea of pruning.  
I. Duplication
```py
class Solution:
    def combinationSum(self, candidates, target):
        Res =[]
        candidates.sort()
        self.backtrack(candidates, Res, [], target, 0)
        return Res
    
    def backtrack(self, nums, Res, temp, remain, start):
        if remain == 0: 
            Res.append(temp[:])
        else: 
            for i in range(start, len(nums)):
                # pre-pruning avoiding useless operation
                if remain < nums[i]: return
                temp.append(nums[i])
                self.backtrack(nums, Res, temp, remain - nums[i], i)
                temp.pop()
```
II.No Duplication  
```py
class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        self.backtrack(candidates, 0, [], res, target)
        return res
        
    def backtrack(self, nums, start, temp, res, remain):
        if remain == 0:
            res.append(temp[:])
        else:
            for i in range(start, len(nums)):
                # skip duplication
                if i > start and nums[i] == nums[i - 1]:
                    continue 
                if remain - nums[start] < 0:
                    return
                temp.append(nums[i])
                self.backtrack(nums, i + 1, temp, res, remain - nums[i])
                temp.pop()
        
```
