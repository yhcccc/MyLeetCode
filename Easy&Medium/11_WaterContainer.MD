  
##Double 
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
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return areaMax
```
