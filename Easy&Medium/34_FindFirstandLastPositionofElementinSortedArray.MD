#### Do not consider the linear method.  
------------------------------------------
**1.Binary Search -> Linear Search**  
The first thing that comes to mind is to use Binary Search first and then Linear Search.  
```py
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums or nums[0] > target or nums[-1] < target:
            return [-1, -1]
        l = len(nums)
        if nums[0] == nums[-1] == target:
            return [0, l - 1]
        ll, lr = 0, l - 1
        while ll <= lr:
            mid = (ll + lr) // 2
            if nums[mid] > target:
                lr = mid - 1
            elif nums[mid] < target:
                ll = mid + 1
            else:
                # Start to linearSearch
                ll = mid - 1
                lr = mid + 1
                while ll >= 0 and nums[ll] == target:
                    ll -= 1
                while lr < l and nums[lr] == target:
                    lr += 1
                return [ll + 1, lr - 1]
        return [-1, -1]
```
--------------------------------------------------
**2.Twice Binary Search**  
```py
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums or nums[0] > target or nums[-1] < target:
            return [-1, -1]
        if nums[0] == nums[-1] == target:
            return [0, len(nums) - 1]
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] >= target:
                hi = mid - 1
            else:
                lo = mid + 1
        if nums[lo] != target:
            return [-1, -1]
        leftIndex = lo
        hi = len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return [leftIndex, hi]
```  
This is optimized binary search below.(Beats 100%)
```py
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            
            mid = (lo + hi) // 2
            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid + 1
        if lo == len(nums) or nums[lo] != target:
            return [-1, -1]
        leftIndex = lo
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2 # Key optimization!!!
            if nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid
        return [leftIndex, hi]
```
In fact, it's hard to get for me.  
Then I learn boundary problem about binary search @ <https://blog.csdn.net/u011523762/article/details/50878613>  
I get the method below, based on <<编程珠玑>>.   
It's most perfect BS, but It performed no better than previous one.
```py
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        lo, hi = -1, len(nums)
        while lo + 1 != hi:
            # Avoid numerical overflow
            mid = lo + (hi - lo) // 2
            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid
        if hi == len(nums) or nums[hi] != target:
            return [-1, -1]
        leftIndex = hi
        hi = len(nums)
        while lo + 1 != hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > target:
                hi = mid
            else:
                lo = mid
        return [leftIndex, lo]
```
