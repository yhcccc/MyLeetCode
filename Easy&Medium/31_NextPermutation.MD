**Single Pass Approach**  
Key: Learn the lexicographically and find the law  
See <https://leetcode.com/problems/next-permutation/solution/>  
```py
class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if l <= 1:
            return
        
        i = l - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = i + 2
            while j < l and nums[j] > nums[i]:
                j += 1
            # Swap Fun. in Py3 is so simple
            nums[i],nums[j-1] = nums[j-1],nums[i]
        # Reverse Fun.
        j = l - 1
        while i + 1 < j:
            nums[i + 1],nums[j] = nums[j],nums[i + 1]
            i += 1
            j -= 1
```
