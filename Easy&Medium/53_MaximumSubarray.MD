--------------------
**1.Greedy**  
O(n)
```py
class Solution:
    def maxSubArray(self, nums):
        res, temp = nums[0], 0
        for num in nums:
            temp += num
            res = max(res, temp)
            if temp < 0:
                temp = 0
        return res
```
```py
class Solution:
    def maxSubArray(self, nums):
        res, temp = nums[0], nums[0]
        for num in nums[1:]:
            temp = max(temp + num, num)
            res = max(res, temp)
        return res
```
----------------------
**2.Divide and conquer**  
<https://leetcode.com/problems/maximum-subarray/discuss/20200/Share-my-solutions-both-greedy-and-divide-and-conquer>
```py
class Solution:
    l, r, m, s = 0, 0, 0, 0
    
    def maxSubArray(self, nums):
        n = len(nums)
        V = self.dac(nums, n)
        return V[2]
        
    def dac(self, nums, n):
        if n == 1:
            return [nums[0] for _ in range(4)]
        V1 = self.dac(nums, n//2)
        V2 = self.dac(nums[n//2:], n - n//2)
        l = max(V1[0], V1[3] + V2[0])
        r = max(V2[1], V1[1] + V2[3])
        m = max(max(V1[2], V2[2]), V1[1] + V2[0])
        s = V1[3] + V2[3]
        return [l, r, m, s]
```
