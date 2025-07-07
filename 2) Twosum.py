class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            if (target - num) in seen:
                return [seen[target - num], i]
            seen[num] = i 
'''

Removes explicit typing (List[int]) if not required.

Avoids intermediate variable (complement).

Is short, clean, and still readable.
'''
