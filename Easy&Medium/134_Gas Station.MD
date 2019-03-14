**One Pass**  
A clever idea:  
I have thought for a long time and got two ideas:  
* If car starts at A and can not reach B. Any station between A and B
can not reach B.(B is the first station that A can not reach.)  
* If the total number of gas is bigger than the total number of cost. There must be a solution.
(Should I prove them?)  
```py
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, total, tank = 0, 0, 0
        for i in range(len(gas)):
            tank = tank + gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                total += tank
                tank = 0
        return start if total + tank >= 0 else -1
```
