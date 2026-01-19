# https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    count_sequence = {}

    def longestSequence(self, key):
        if key not in self.count_sequence: return 0

        if self.count_sequence[key] > 1:
            return self.count_sequence[key]

        val_key = 1 + self.longestSequence(key+1)
        self.count_sequence[key] = val_key

        return val_key

    def longestConsecutive(self, nums: List[int]) -> int:
        self.count_sequence = {}
        for n in nums:
            self.count_sequence[n] = 0

        max_sequence = 0
        for k in self.count_sequence.keys():
            sequence_starting_in_k = self.longestSequence(k)
            self.count_sequence[k] = sequence_starting_in_k
            max_sequence = max(max_sequence, sequence_starting_in_k)
        
        return max_sequence
