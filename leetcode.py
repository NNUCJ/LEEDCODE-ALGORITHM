
#
# nums = [2,3,1,2,4,3]
# n = 7
#
# class Solution:
#     def minSubArrayLen(self, s: int, nums):
#         if not nums:
#             return 0
#         else:
#             left = 0
#             tmp_sum = 0
#             res = float('inf')
#             for right in range(len(nums)):
#                 tmp_sum += nums[right]
#                 while tmp_sum >= s:
#                     res = min(res, right - left + 1)
#                     tmp_sum -= nums[left]
#                     left += 1
#         return res if res != float('inf') else 0
#
# fun = Solution()
# res = fun.minSubArrayLen(n, nums)
# print(res)

# leetcode378
# from typing import List
# class Solution:
#     def kthSmallest(self, matrix: List[List[int]], k):
#         n = len(matrix)
#         def check_mid(mid):
#             i, j = n-1, 0  # i 表示行，j表示列
#             cnt = 0
#             while i >=0 and j <= n-1:
#                 if matrix[i][j] <= mid:
#                     cnt += i + 1   # 加i的原因是最后一列的数肯定是最大的，因此小于mid的个数可以直接加行数
#                     j += 1
#                 else:
#                     i -= 1
#             return cnt >= k
#
#         # 确定二分法的两个区间
#         left, right = matrix[0][0], matrix[n-1][n-1]
#         while left < right:
#             mid = (left + right) // 2
#             if check_mid(mid):
#                right = mid
#             else:
#                 left = mid + 1
#         return left
#
#
# matrix = [
#              [1, 5, 9],
#              [10, 11, 13],
#              [12, 13, 15]
#          ]
#
# S = Solution()
# res = S.kthSmallest(matrix, k=8)
# print(res)
from typing import List
import collections
#
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
#
# def create_Bitree(data, index):
#     Pnode = None
#     if index < len(data):
#         if data[index]  is  None:
#             return Pnode
#         Pnode = TreeNode(data[index])
#         Pnode.left = create_Bitree(data, 2*index + 1)
#         Pnode.right = create_Bitree(data, 2 * index + 2)
#
#     return Pnode

# data = [5,4,8,11,None,13,4,7,2,None,None,None,1]
# for i in range(len(data)):
#     Pnode = create_Bitree(data, 0)
# print(Pnode.left.val)


# class Solution:
#     def hasPathSum(self, root: TreeNode, sum: int) -> bool:
#         if not root:  # 可能存在树为空的情况
#             return False
#         que_node = collections.deque([root])   # 记录遍历的节点
#         que_val = collections.deque([root.val])  # 记录遍历节点的value
#         while que_node:
#             now = que_node.popleft()
#             temp_val = que_val.popleft()
#             if not now.left and not now.right:   # 处于叶子节点位置判断与目标值的关系
#                 if temp_val == sum:
#                     return True
#                 continue
#
#             if now.left:
#                 que_node.append(now.left)
#                 que_val.append(now.left.val + temp_val)
#
#             if now.right:
#                 que_node.append(now.right)
#                 que_val.append(now.right.val + temp_val)
#         return False
#
# data = [5,4,8,11,None,13,4,7,2,None,None,None,1]
#
# Pnode = create_Bitree(data, 0)
# # print(Pnode.left.left.val)
# sum = 22
# S = Solution()
# out = S.hasPathSum(Pnode, sum)
# print(out)

### leetcode 面试题16.11
# class Solution:
#     def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
#         res = []
#         if k == 0:
#             res.append(0)
#         else:
#             for i in range(k+1):
#                 tmp = i*shorter + (k-i)*longer
#                 res.append(tmp)
#         res_ = sorted(res)
#         return res_
#
# S =Solution()
# res = S.divingBoard(1, 1, 0)
# print(res)
# class Solution:
#     def maxProfit(self, prices):
#         if not prices:
#             return 0
#
#         n = len(prices)
#         dp = [[-prices[0], 0, 0]] + [[0] * 3 for _ in range(n - 1)]  # 构建dp数组存储状态
#
#         for i in range(1, n):
#             dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])
#             dp[i][1] = dp[i - 1][0] + prices[i]
#             dp[i][2] = max(dp[i - 1][1], dp[i - 1][2])
#
#         return max(dp[n - 1][1], dp[n - 1][2])

### leetcode120 三角形最小路径和

# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#
#         n = len(triangle)
#         dp = [[0] * n for _ in range(n)]
#         dp[0][0] = triangle[0][0]
#
#         # dp[0] = triangle[0][0]
#         for i in range(1, n):
#             dp[i][0] = dp[i - 1][0] + triangle[i][0] # 定义最左侧状态转移方程
#             for j in range(1, i):
#                 dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j] # 一般情况
#             dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]  # 定义的最右侧
#         print("dp : {}".format(dp))
#         return min(dp[n - 1])


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def create_Bitree(data, index):
    Pnode = None
    if index < len(data):
        if data[index] is None:
            return Pnode
        Pnode = TreeNode(data[index])
        Pnode.left = create_Bitree(data, 2 * index + 1)
        Pnode.right = create_Bitree(data, 2 * index + 2)

    return Pnode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def generateTrees(self, n: int):
#         def generateTrees(start, end):
#             if start > end:
#                 return [None,]

#             Tree_list = []

#             for i in range(start, end+1):  # 遍历确定根节点

#                 left_trees = generateTrees(start, i-1)

#                 right_tree = generateTrees(i+1, end)

#                 for l in left_trees:
#                     for r in right_tree:
#                         roottree = TreeNode(i)
#                         roottree.left = l
#                         roottree.right = r
#                         Tree_list.append(roottree)
#             return Tree_list
#         return generateTrees(1, n) if n else []


## 前序遍历
def preordef(root):
    if root == None:
        return
    # print(root.val, end=' ')

    preordef(root.left)
    preordef(root.right)



if __name__ == '__main__':
    data = [3,4,5,1,3,None,1]
    pnode = create_Bitree(data, 0)
    preordef(pnode)
    # triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    # S = Solution()
    # re = S.generateTrees(3)
    # tree_listpreordef(re[0])
    # for i in re:
    #     tree_list = preordef(i)
        # print(tree_list)
        # for tree in re:
    #     print(tree.val)
    # print(re[0].left.val)


    # [
    #     [2],
    #    [3, 4],
    #   [6, 5, 7],
    #  [4, 1, 8, 3]
    # ]
