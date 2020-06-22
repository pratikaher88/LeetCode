# To find out Kth largest element in a List

# https://leetcode.com/problems/kth-largest-element-in-an-array/
# LeetCode 215

import random

class Solution:

    def quickselect(self, arr, k):

        N = len(arr)
        left = 0
        right = N-1

        while left<=right:

            choosenPivotIndex = random.randrange(left,right)

            finalIndexOfChoosenPivot = self.partition(arr, left, right, choosenPivotIndex)

            if finalIndexOfChoosenPivot == N-k:
                return arr[finalIndexOfChoosenPivot]

            elif finalIndexOfChoosenPivot > N-k :
                right = finalIndexOfChoosenPivot - 1
            else:
                left = finalIndexOfChoosenPivot + 1




    def partition(self, arr, left, right, pivotIndex):

        pivotValue = arr[pivotIndex]

        lesserItemsTailIndex = left

        self.swap(arr, pivotIndex, right)

        for i in range(left, right):

            if arr[i] < pivotValue:
                self.swap(arr, i, lesserItemsTailIndex)
                lesserItemsTailIndex += 1

        self.swap(arr, right, lesserItemsTailIndex)

        return lesserItemsTailIndex


    def swap(self, arr, first, second):

        temp = arr[first]
        arr[first] = arr[second]
        arr[second] = temp



S = Solution()


print(S.quickselect([1,3,5,7,2], 2))


# Time Complexity : O(n) - Average case - O(n^2) Worst Case
# Space Complexity : O(1)

