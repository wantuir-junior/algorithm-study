class Solution:
    def longestConsecutiveSequence(self, nums: list[int]) -> int:
        nums_set = set(nums)
        longest_seq = 0

        for num in nums:
            if (num-1) not in nums_set:
                seq_lenght = 0
                while (num + seq_lenght) in nums_set:
                    seq_lenght += 1
                
                longest_seq = max(seq_lenght, longest_seq)

        return longest_seq