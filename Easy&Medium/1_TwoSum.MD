-----------------------------------------------------------
（未使用hash表：字典）思路关键：a = t - b 
```py
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        Index = []
        i = 0
        for num_1 in nums:
            num_2 = target - num_1
            if num_2 in nums:
                j = nums.index(num_2)
                # 此为关键的判断，避免了取两次
                if j < i:
                    Index += [j, i]
            i += 1
        return Index
```

-----------------------------------------------------------
（使用hash表：字典）思路关键：a = t - b （提交不成功，输出格式问题懒得改了）
```py
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        d = collections.defaultdict(int)
        index = []
        # 枚举同时得到下表和数据
        for i,num in enumerate(nums):  
            if num not in d:
                d[target - num] = i
            else:
                index.append([d[num],i])
        return index
```
