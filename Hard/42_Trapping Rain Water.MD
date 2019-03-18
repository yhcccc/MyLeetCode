My Code:
TC: O(n^2)(worst: n+(n-1)+...+1=n(n-1)/2).  
Since my code benefits from the defined function in Py3 max() that runs faster, it performs well in submission.  
Just find the max height(bidirectional), and use ```- sum(height[m+1:m_cur])``` can skip many O(1) operation.
```py
def trap(self, height: List[int]) -> int:
        
      def helper(high, m, flag, temp):
          if flag:
              
              if m == 0: return temp
              high_cur = max(height[0:m])
              if high_cur == 0: return temp
              
              m_cur = height.index(high_cur)
              water = temp + high_cur * (m - m_cur - 1) - sum(height[m_cur+1:m])
              water = helper(high_cur, m_cur, True, water)
          else:
              if m+1 == len(height): return temp
              high_cur = max(height[m+1:])
              if high_cur == 0: return temp
              
              m_cur = height[m+1:].index(high_cur) + m + 1
              water = temp + high_cur * (m_cur - m - 1) - sum(height[m+1:m_cur])
              water = helper(high_cur, m_cur, False, water)
          return water

      if not height: return 0
      high = max(height)
      if high == 0: return 0
      m = height.index(high)
      water_l = helper(high, m, True, 0)
      water_r = helper(high, m, False, 0)
      return water_l + water_r
    
```

Other see Solution.
