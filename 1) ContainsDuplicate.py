class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
'''
set(nums) removes duplicates.

If any duplicate was present, the length of the set will be less than the length of the original list.

So if lengths don’t match → duplicates exist → return True.

len(nums) != len(set(nums)) is the fastest one-liner for duplicates.

'''