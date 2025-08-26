"""
给你一个下标从 0 开始的二维整数数组 dimensions。

对于所有下标 i（0 <= i < dimensions.length），dimensions[i][0] 表示矩形 i 的长度，而 dimensions[i][1] 表示矩形 i 的宽度。

返回对角线最 长 的矩形的 面积 。如果存在多个对角线长度相同的矩形，返回面积最 大 的矩形的面积。


题解:
    硬算法:对角线长度=长平方+宽平方,记录相同数字的缓存
"""
from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_area = 0
        max_l = 0
        for i in dimensions:
            a = i[0] * i[0] + i[1] * i[1]
            if a > max_l:
                max_l = a
                max_area = i[0] * i[1]
            elif a == max_l:
                max_l = a
                max_area = max(i[0] * i[1], max_area)
        return max_area


print(Solution().areaOfMaxDiagonal([[6,5],[8,6],[2,10],[8,1],[9,2],[3,5],[3,5]]

))
