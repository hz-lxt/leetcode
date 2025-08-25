"""
给你一个大小为 m x n 的矩阵 mat ，请以对角线遍历的顺序，用一个数组返回这个矩阵中的所有元素。
输入：mat = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,4,7,5,3,6,8,9]

题解：
   获取所有对角线,奇数对角线正序,偶数对角线倒叙
   难点:获取所有对角线
   node = mat[x][y]
   n = len mat m= len mat[0]
   对角线数量=n+m-1,得到这个结论可以把对角线拆成两部分,n表示所有第一个节点x=0的,最后一条x=0后的节点为y从1递增至m,故对角线数量=n+m-1
   获取对角线:可以根据上面的过程分成两个条件判断,其中每个判断有两个子条件判断:
        1 正序,当对角线数量<m,x=0,y=i,对角线数量>m,x=数量-m+1(因为横着看完了需要竖着看了),y=
        2 倒叙,当对角线数量<n,y=0,对角线数量>n,y=数量-n+1
"""
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ret_mat = []
        n, m = len(mat), len(mat[0])
        for i in range(n + m - 1):
            if i % 2:
                x = 0 if i < m else i - m + 1
                y = i if i < m else m - 1
                while x < n and y >= 0:
                    ret_mat.append(mat[x][y])
                    x += 1
                    y -= 1
            else:
                x = i if i < n else n - 1
                y = 0 if i < n else i - n + 1
                while y < m and x >= 0:
                    ret_mat.append(mat[x][y])
                    x -= 1
                    y += 1
        return ret_mat


print(Solution().findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
