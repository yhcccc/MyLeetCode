---------
双指针法
时间复杂度：O(n);空间：O(1)
```py
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = len(height)
        areaMax = 0
        i = 0; j = l - 1
        while(i != j):
            areaCur = (j - i) * min(height[i], height[j])
            if areaCur > areaMax:
                areaMax = areaCur
            # find the higher line to overcome decrease in x
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return areaMax
```
Faster
```py
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0; j = len(height) - 1
        s = 0
        while i < j:
            s = max(s, min(height[i], height[j]) * (j - i))
            if height[i] > height[j]:
                h = height[j]
                while i < j and height[j-1] < h:
                    j -= 1
                j -= 1
            else:
                h = height[i]
                while i < j and height[i+1] < h:
                    i += 1
                i += 1
        return s
```
