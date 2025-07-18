from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in num_set:
            # Start a new sequence only if n is the start
            if n - 1 not in num_set:
                length = 1
                current = n

                while current + 1 in num_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest
'''Convert nums to a set for O(1) lookups.

Loop through the set:

Only start counting when n - 1 is not in the set — that means n is the start of a sequence.

Count how long the consecutive sequence goes (n, n+1, n+2, ...).

Track the max length found.Concept	Insight
HashSet	For O(1) lookup and to remove duplicates
Only start from “beginners”	if n - 1 not in set:
Time Complexity	O(n) total (not O(n²))
Why not sort?	Sorting takes O(n log n) — violates constraints

Mistakes to Avoid:
Sorting the array (O(n log n) = ❌)

Not using a set — leads to O(n²)

Not checking for n-1 before starting the sequence

Counting duplicate elements'''