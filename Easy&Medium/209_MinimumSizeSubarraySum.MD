**brute force[Time limit exceeded]**  
 O(n^2)  
 ```py
 class Solution:
    def minSubArrayLen(self, s, nums):
        if not nums: return 0
        ans = 2147483648
        n = len(nums)
        sums = [0 for _ in range(n)]
        sums[0] = nums[0]
        for i in range(1, n):
            sums[i] = sums[i - 1] + nums[i]
        for i in range(n):
            for j in range(i, n):
                sum_ = sums[j] - sums[i] + nums[i]
                if sum_ >= s:
                    ans = min(ans, j - i + 1)
                    break
        return ans if ans != 2147483648 else 0
 ```
 
 **Binary Search**  
 O(nlog(n))  
 My Code(Not Good):
 ```py
 class Solution:
    def minSubArrayLen(self, s, nums):
        # Divide and conquer
        n = len(nums)
        ans = n + 1
        sums = [0 for _ in range(n + 1)]
        # sums[0]=0 : Meaning that it is the sum of first 0 elements
        # sums[1]=A[0] : Sum of first 1 elements
        # ans so on...
        for i in range(1, n + 1):
            sums[i] = sums[i - 1] + nums[i - 1]
        for i in range(1, n + 1):
            to_find = s + sums[i - 1]
            bound = self.lower_bound(sums[i:], to_find)
            if bound == -1: return 1
            if bound != n - i + 1:
                ans = min(ans, bound + 1)
        return ans if ans <= n else 0
    
    def lower_bound(self, nums, target):
        low, high = -1, len(nums)
        while low + 1 != high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid
            else: # >=
                high = mid
        return high if high <= len(nums) else -1
 ```
 A better one:
 ```py
 class Solution:
    def minSubArrayLen(self, target, nums):
        result = len(nums) + 1
        for idx, n in enumerate(nums[1:], 1):
            nums[idx] = nums[idx - 1] + n
        left = 0
        for right, n in enumerate(nums):
            if n >= target:
                left = self.find_left(left, right, nums, target, n)
                result = min(result, right - left + 1)
        return result if result <= len(nums) else 0

    def find_left(self, left, right, nums, target, n):
        while left < right:
            mid = (left + right) // 2
            if n - nums[mid] >= target:
                left = mid + 1
            else:
                right = mid
        return left
 ```
 
 **2 pointers**  
 O(n)  
 ```py
 class Solution:
    def minSubArrayLen(self, s, nums):
        n = len(nums)
        ans = n + 1
        left = 0
        sum_ = 0
        for i in range(n):
            sum_ += nums[i]
            while sum_ >= s:
                ans = min(ans, i + 1 - left)
                sum_ -= nums[left]
                left += 1
        return ans if ans <= n else 0
 ```
