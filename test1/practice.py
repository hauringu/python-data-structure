# -*- coding: utf-8 -*- 
# @Time : 2021/4/12 16:32 
# @Author : HGuoo 
# @File : practice.py


def findNumberIn2DArray(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    l = 0
    r = len(matrix) - 1
    while l <= r:
        mid = (l + r) // 2
        if matrix[mid][len(matrix[mid]) - 1] == target:
            return True
        elif matrix[mid][len(matrix[mid]) - 1] > target:
            r = mid - 1
        else:
            l = mid + 1
    left = 0
    right = len(matrix[l]) - 1
    while left <= right:
        mid = (left + right) // 2
        if matrix[l][mid] == target:
            return True
        elif matrix[l][mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False


matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
target = 5
print(findNumberIn2DArray(0, matrix, target))
