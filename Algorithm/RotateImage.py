# -*- coding:utf-8 -*-
'''
    题目：旋转图像
    给定一个 n × n 的二维矩阵表示一个图像。

    将图像顺时针旋转 90 度。
    说明：
    你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。 请不要 使用另一个矩阵来旋转图像。

    示例 1:
    给定 matrix =
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ],

    原地旋转输入矩阵，使其变为:
    [
        [7,4,1],
        [8,5,2],
        [9,6,3]
    ]

    示例 2:
    给定 matrix =
    [
        [ 5, 1, 9,11],
        [ 2, 4, 8,10],
        [13, 3, 6, 7],
        [15,14,12,16]
    ],

    原地旋转输入矩阵，使其变为:
    [
        [15,13, 2, 5],
        [14, 3, 4, 1],
        [12, 6, 8, 9],
        [16, 7,10,11]
    ]

'''

class Solution(object):
    def rotate(self, matrix):
        '''
        :type matrix: List[List[int]]
        :rtype: void (Do not return anything, modify matrix in-place instead.)
        '''
        if len(matrix) == 0:
            return
        h = len(matrix)
        w = len(matrix[0])
        for i in xrange(0, h):
            for j in xrange(0, w/2):
                matrix[i][j], matrix[i][w-j-1] = matrix[i][w-j-1], matrix[i][j]

        for i in xrange(0, h):
            for j in xrange(0, w-1-j):
                matrix[i][j], matrix[w-1-j][h-1-i] = matrix[w-1-j][h-1-i], matrix[i][j]
