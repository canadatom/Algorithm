class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """

        # save index of word1 to a list
        # save index of word2 to a list
        # loop over both indexes and find the min of both index range
        
        word1_indexes = [ i for i in range(len(words)) if word1 == words[i] ]
        word2_indexes = [ i for i in range(len(words)) if word2 == words[i] ]
        
        return min([ abs(i - j) for i in word1_indexes for j in word2_indexes ])

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        # nums   5 0 4 3 0 2
        # i      0 1 2 3 4 5
        # count  0 1 1 1 2 2
        #        5 4 3 2 0 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                nums[i-count] = nums[i]
        for i in range(count):
            nums[len(nums) - 1 - i] = 0

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals = sorted(intervals, key=lambda x:x.start)
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False
        return True