**Deeper Binary Search**  
Key: "If nums[mid] and target are "on the same side" of nums[0], just take nums[mid]".  
```py
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ll = 0; lr = len(nums) - 1
        while lr >= ll:
            mid = (lr + ll) // 2
            # Take care of the situation 'target == nums[0]'.
            if (target < nums[0]) == (nums[mid] < nums[0]):
                if target > nums[mid]:
                    ll = mid + 1
                elif target < nums[mid]:
                    lr = mid - 1
                else:
                    return mid
            elif target < nums[0]:
                ll = mid + 1
            elif target > nums[0]:
                lr = mid - 1
            else:
                return 0
        return -1
```
