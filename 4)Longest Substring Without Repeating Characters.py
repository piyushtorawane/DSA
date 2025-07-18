class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            if s[right] in char_index and char_index[s[right]] >= left:
                left = char_index[s[right]] + 1
            char_index[s[right]] = right
            max_len = max(max_len, right - left + 1)

        return max_len
'''char_index: dictionary to store the last index of every character.

left: start of the sliding window.

right: end of the sliding window (iterator).

max_len: stores the maximum length found.
Move the window’s left boundary only when a repeat is detected. Store where each character was last seen so you can skip to just after its last appearance."Time: O(n) (each character visited once)

Space: O(min(n, m))
where m = character set size (exampl 26 for lowercase letters, 128 for ASCii)

'''