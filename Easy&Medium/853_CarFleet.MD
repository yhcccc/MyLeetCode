-------------------------------
## 1.Stack  
先排序，需花费O(NlogN)的时间；再根据离终点距离，由远及近地出栈，比较每一次出栈车辆的达到时间(target - position) / speed。  
空间：O(N)  
```py
class Solution:
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        cars = sorted(zip(position, speed)) #默认reverse=False
        time = [float (target - p)/s for p, s in cars]
        Numf = 0
        while len(time) > 1:
            lead = time.pop()
            if lead < time[-1]: #若慢于领头车，则领头车永远不能被追上，单独为1个车队
                Numf += 1
            else:
                time[-1] = lead
        return Numf + bool(time)
```
