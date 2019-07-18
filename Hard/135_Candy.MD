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
