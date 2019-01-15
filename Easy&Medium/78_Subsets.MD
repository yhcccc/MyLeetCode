**1.BackTrack**
```py
class Solution:
    def subsets(self, nums):
        res = []
        self.backtrack(0, res, [], nums)
        return res
        
    def backtrack(self, start, res, temp, nums):
        res.append(temp[:])
        for i in range(start, len(nums)):
            temp.append(nums[i])
            self.backtrack(i + 1, res, temp[:], nums)
            temp.pop(-1)
```
Modify it:
```py
class Solution:
    def subsets(self, nums):
        res = []
        self.backtrack(0, res, [], nums)
        return res
        
    def backtrack(self, start, res, temp, nums):
        res.append(temp[:])
        for i in range(start, len(nums)):
            self.backtrack(i + 1, res, temp + [nums[i]], nums)
```
