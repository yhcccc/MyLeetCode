---------------------------------------------------------
**15** 这题是真的有毒。达到目的不难，但输出重复是个很蛋疼的问题。两种方法：  
1.借用2Sum的思路   
时间: O(N^2)
这里不能对j采用如下方法  
```py
if j < l - 1 and nums[j] == nums[j+1]:
    continue
```
因为3个0就无法输出了；  
但是这样的话就会出现输出重复了，所以不得不用到set(),如下
```py
class Solution():
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i-1]:
                continue
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v, -v-x, x))
        return list(map(list, res))
```
2.滑动窗口法 
O(N^2)  
用两个指针，可以节省时间
```py
class Solution():
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        n = len(nums)
        if n < 3 or nums[0] > 0 or nums[n-1] < 0:
            return res
        
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, n-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1            
        return res
```
**16** 几乎与上题相同，只用小改一下：  
```py
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = float("inf") 
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, n-1
            while l < r:
                s = nums[i] + nums[l] + nums[r] - target
                if abs(s) < abs(res):
                    res = s
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    return target
        return target + res
```
