**two pass**  
Count;O(m+n) space
```py
class Solution:
    def sortColors(self, nums):
        counter = [0, 0, 0]
        for num in nums:
            if num == 0:
                counter[0] += 1
            elif num == 1:
                counter[1] += 1
            else:
                counter[2] += 1
        nums[:] = [0] * counter[0] + [1] * counter[1] + [2] * counter[2]
```
**one pass in place solution** 
```py
class Solution:
    def sortColors(self, nums):
        i, j = 0, 0
        for k in range(len(nums)):
            v = nums[k]
            nums[k] = 2
            if v < 2:
                nums[j] = 1
                j += 1
            if v == 0:
                nums[i] = 0
                i += 1
```
[Dutch national flag problem](https://en.wikipedia.org/wiki/Dutch_national_flag_problem)  
**one pass in place solution**
```py
class Solution:
    def sortColors(self, nums):
        red, white, blue = 0, 0, len(nums) - 1
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1; white += 1
            elif nums[white] == 1:
                white += 1
            elif nums[white] == 2:
                nums[blue], nums[white] = nums[white], nums[blue]
                blue -= 1
```
