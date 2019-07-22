You are giving candies to these children subjected to the following requirements:  

* Each child must have at least one candy.  
* Children with a higher rating get more candies than their neighbors.  

```
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        l2r = [1 for _ in range(n)]
        r2l = [1 for _ in range(n)]
        
        for i in range(n-1):
            if ratings[i] < ratings[i+1]:
                l2r[i+1] = l2r[i] + 1
                
        for i in range(n-1, 0, -1):
            if ratings[i] < ratings[i-1]:
                r2l[i-1] = r2l[i] + 1  
        
        res = zip(l2r, r2l)
        candies = sum(map(max, res))
        return candies
```

```
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candy = [1 for _ in range(n)]
        
        for i in range(n-1):
            if ratings[i] < ratings[i+1]:
                candy[i+1] = candy[i] + 1
                
        for i in range(n-1, 0, -1):
            if ratings[i] < ratings[i-1]:
                candy[i-1] = max(candy[i] + 1, candy[i-1])

        candies = sum(candy)
        return candies
```
```
class Solution:
    def count(self, n):
        return (n * (n + 1)) // 2
    
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n <= 1:
            return n
        
        candies = 0
        up, down = 0, 0
        old_slope = 0
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                new_slope = 1
            elif ratings[i] < ratings[i-1]:
                new_slope = -1
            else:
                new_slope = 0
            if (old_slope < 0 and new_slope >= 0) or \
                (old_slope > 0 and new_slope == 0):
                candies += self.count(up) + self.count(down) + max(up, down)
                up, down = 0, 0
            if new_slope > 0:
                up += 1
            if new_slope < 0:
                down += 1
            if new_slope == 0:
                candies += 1
            old_slope = new_slope
        candies += self.count(up) + self.count(down) + max(up, down) + 1
        return candies
```
