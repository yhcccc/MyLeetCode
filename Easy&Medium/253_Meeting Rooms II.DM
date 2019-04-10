**1.Priority Queues**  
TC: O(NlogN); SC: O(N)  
```py
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0
        intervals.sort(key = lambda x: x.start)
        rooms = []
        heapq.heappush(rooms, intervals[0].end)
        for interval in intervals[1:]:
            if interval.start >= rooms[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, interval.end)
        return len(rooms) 
```
**2.Chronological Ordering**  
TC: O(NlogN); SC: O(N)  
```py
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0
        rooms = 0
        start_time = sorted([i.start for i in intervals])
        end_time = sorted([i.end for i in intervals])
        L = len(intervals)
        s_ptr, e_ptr = 0, 0
        while s_ptr < L:
            if start_time[s_ptr] < end_time[e_ptr]:
                rooms += 1
                s_ptr += 1
            else:
                s_ptr += 1
                e_ptr += 1
        return rooms
```
