[My solution explanation](https://leetcode.com/problems/k-closest-points-to-origin/discuss/220326/Python3-Solution-using-QuickSelect-and-PriorityQueue)  

**1.Sort**  
O(NlogN)
```py
class Solution:
    def kClosest(self, points, K):
        points.sort(key = lambda x: x[0]**2 + x[1]**2)
        return points[:K]
```

**2.QuickSelect**  
Average O(N); Worst O(N^2)
```py
class Solution(object):
    def kClosest(self, points, K):
        dist = lambda i: points[i][0]**2 + points[i][1]**2

        def Medium3(left, right):
            center = (left + right) // 2
            if dist(left) > dist(center):
                points[left], points[center] = points[center], points[left]
            if dist(left) > dist(right):
                points[left], points[right] = points[right], points[left]
            if dist(center) > dist(right):
                points[center], points[right] = points[right], points[center]
            # Invariant: points[left] <= points[center] <= points[right]
            points[center], points[right - 1] = points[right - 1], points[center]
            return dist(right - 1)

        def Qselect(k, left, right):
            if left < right:
                pivot = Medium3(left, right)
                i = left; j = right - 1
                while i < j:
                    i += 1
                    while dist(i) < pivot: i += 1
                    j -= 1
                    while dist(j) > pivot: j -= 1
                    if i < j:
                        points[i], points[j] = points[j], points[i]
                points[i], points[right - 1] = points[right - 1], points[i]
                if k <= i:
                    Qselect(k, left, i - 1)
                elif k > i + 1:
                    Qselect(k, i + 1, right)
                    
        Qselect(K, 0, len(points) - 1)
        return points[:K]
```

**3.PriorityQueue(Heap)**  
O(N + klogN)
```py
import queue
class Solution:
    def kClosest(self, points, K):
        dist = [point[0]**2 + point[1]**2 for point in points]
        q = queue.PriorityQueue()
        
        for i in range(len(points)):
            q.put((-dist[i], points[i]))
            if q.qsize() > K:
                q.get()
        
		    res = []
        while K > 0:
            point = q.get()[1]
            res.append(point)
            K -= 1
        return res
```
