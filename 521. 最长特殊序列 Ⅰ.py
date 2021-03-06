#
# 给定两个字符串，你需要从这两个字符串中找出最长的特殊序列。最长特殊序列定义如下：该序列为某字符串独有的最长子序列（即不能是其他字符串的子序列）。
#
# 子序列可以通过删去字符串中的某些字符实现，但不能改变剩余字符的相对顺序。空序列为所有字符串的子序列，任何字符串为其自身的子序列。
#
# 输入为两个字符串，输出最长特殊序列的长度。如果不存在，则返回 -1。
#
# 示例 :
#
# 输入: "aba", "cdc"
# 输出: 3
# 解析: 最长特殊序列可为 "aba" (或 "cdc")
# 说明:
#
# 两个字符串长度均小于100。
# 字符串中的字符仅含有 'a'~'z'。

# 分析 =============================================================================
# 这道题目看起来觉得很难，但其实一点也不难……
#
# 如果两个字符串长度不相等，那么最长的特殊序列就是给定的两个字符串中那个比较长的……它绝对不是另一个字符串的子序列。
#
# 如果两个字符串长度相等呢？如果两个字符串一模一样，那么没有最长的特殊序列。无论A的什么子序列，都可以在B中找到相应的子序列。这时要返回-1。
#
# 如果两个字符串长度相等并且两个字符串不是一模一样的，比如abcdef和abcdeg，那么最长的特殊序列就是两个字符串之中一个……
class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        return -1 if (len(a) == len(b)) else max(len(a), len(b))
s = Solution()
test1 = "cd"
test2 = "cd"
print(s.findLUSlength(test1, test2))