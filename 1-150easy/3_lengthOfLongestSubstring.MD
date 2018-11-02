-------------------------------------------------
## 最大字串，采用滑动窗口的方法，调整[j, i]来找到最大字串   
 时间复杂度T(N)=O(N),最多取完i所有值-N个步骤   
 空间复杂度：Hash表=O(min(m,n)).   
    
```py
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        lmax = 0
        d = {} #dict--hash表
        j = 0
        for i in range(len(s)):
            # 若d中不存在或上次定位已覆盖掉本次重复的key
            if d.get(s[i]) is None or d[s[i]] < j: 
                d[s[i]] = i
                l = i - j + 1
                if l > lmax:
                    lmax = l
            else:
                # 重复时滑动左边界，移至第一个已重复key的右边一位（这是更加优化的方法，一步到位）
                j = d[s[i]] + 1
                d[s[i]] = i
        return lmax
```
