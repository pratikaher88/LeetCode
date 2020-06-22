#https://leetcode.com/problems/find-median-from-data-stream/

#Leecode 295

from heapq import heappush, heappop

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []
        self.large = []

    def addNum(self, num):

        if not self.small or num <= -self.small[0]:
            # push to small part
            heappush(self.small, -num)
        else:
            # push to large part
            heappush(self.large, num)

        self.rebalance()

    def rebalance(self):

        if len(self.small) - len(self.large) == 2:
            heappush(self.large, -1 * heappop(self.small))
        elif len(self.large) - len(self.small) == 2:
            heappush(self.small, -1 * heappop(self.large))

    def findMedian(self):

        if len(self.large) == len(self.small):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return -float(self.small[0]) if len(self.small) > len(self.large) else float(self.large[0])


# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# Time Complexity : O(logn)
# Space Complexity : O(n)
