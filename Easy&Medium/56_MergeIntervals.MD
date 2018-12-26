**1.Connected Components(Gragh)**  
If we draw a graph (with intervals as nodes) that contains undirected edges between all pairs of intervals that overlap, then all intervals in each connected component of the graph can be merged into a single interval.  
More details @ <https://leetcode.com/problems/merge-intervals/solution/>  
Even though the result is **Time Limit Exceeded**, the gragh method used is important.
```py
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def overlap(self, a, b):
        return a.start <= b.end and b.start <= a.end
    
    # generate graph where there is an undirected edge between intervals u
    # and v if u and v overlap.
    def build_gragh(self, intervals):
        gragh = collections.defaultdict(list)
        
        for i, interval_i in enumerate(intervals):
            for j in range(i+1, len(intervals)):
                if self.overlap(interval_i, intervals[j]):
                    gragh[interval_i].append(intervals[j])
                    gragh[intervals[j]].append(interval_i)
        return gragh
    
    # gets the connected components of the interval overlap graph.
    def get_components(self, gragh, intervals):
        visited = set()
        com_number = 0
        nodes_in_comp = collections.defaultdict(list)
        
        def mark_component_dfs(start):
            stack = [start]
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    nodes_in_comp[com_number].append(node)
                    stack.extend(gragh[node])
            
        # gets the connected components of the interval overlap graph.
        for interval in intervals:
            if interval not in visited:
                mark_component_dfs(interval)
                com_number += 1
                
        return nodes_in_comp, com_number
    
    # merges all of the nodes in this connected component into one interval.
    def merge_node(self, nodes):
        min_start = min(node.start for node in nodes)
        max_end = max(node.end for node in nodes)
        return Interval(min_start, max_end)
    
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        gragh = self.build_gragh(intervals)
        nodes_in_comp, number_of_comps = self.get_components(gragh, intervals)
        
        # all intervals in each connected component must be merged.
        return [self.merge_node(nodes_in_comp[comp]) for comp in range(number_of_comps)]
```

**2.Sorting**  
```py
class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x.start)

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1].end = max(merged[-1].end, interval.end)

        return merged
```
Optimized
```py
class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        for i in sorted(intervals, key = lambda x: x.start):
            if res and i.start <= res[-1].end:
                res[-1].end = max(res[-1].end, i.end)
            else:
                res.append(i)
        return res
```
