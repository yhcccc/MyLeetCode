<https://leetcode.com/problems/subarray-sums-divisible-by-k/solution/>
```py
class Solution:
    def subarraysDivByK(self, A, K):
        P = [0]
        for x in A:
            P.append((P[-1] + x) % K)
            
        count = collections.Counter(P)
        return sum(v*(v-1)//2 for v in count.values())
```
