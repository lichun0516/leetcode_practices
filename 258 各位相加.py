#
# 给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。
#
# 示例:
#
# 输入: 38
# 输出: 2
# 解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于 2 是一位数，所以返回 2。
# 进阶:
# 你可以不使用循环或者递归，且在 O(1) 时间复杂度内解决这个问题吗？
class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        if len(s) < 2:
            return num
        sum_s = 0
        while len(str(s)) > 1:
            for i in s:
                sum_s += int(i)
            if len(str(sum_s)) < 2:
                break
            else:
                s = str(sum_s)
                sum_s = 0
        return sum_s

    # --------------------------------------------------------------------
    #
    # 在草稿纸上写一写：
    #
    # 0～9
    # 的结果就是0～9
    #
    # 10～18
    # 的结果是1、2、3 …… 9
    #
    # 19～27
    # 的结果是1、2、3 …… 9
    #
    # 可以发现，0
    # 属于特殊情况，后面每9个数字就一次循环，1～9
    # 一直循环下去，而且结果等于num对9取余，这同样适用于num = 0
    # 的情况。
    #
    # 拿题目的例子验证一下，38 % 9 = 2，看来没错
    #
    # 但其实还存在问题，18 % 9 = 0，但18对应的结果应该是9(1 + 8 = 9)，那么我们可以再稍作修改，结果 = (num - 1) % 9 + 1，这次是正确的。
    # 对 num%9 中18 的特殊情况， (num+1-1)%9 = (num%9 + 1%9 -1%9)%9 ,分类分子保留+1还是-1，保留+1时结果仍为0，保留-1时结果为9（正确）。
    # 因此， （num%9 -1%9)%9 +1%9%9 = (num-1)%9 +1
    # 代码就非常简单了，只需两行：
    # 因此不会出现结果为0的情况。因为 (x + y) % z = (x % z + y % z) % z，又因为 x % z % z = x % z，
    # 因此结果为 (num - 1) % 9 + 1，只模除9一次，并将模除后的结果加一返回。
        if num < 10:
            return num
        else:
            return (num-1) % 9 + 1

s = Solution()
print(s.addDigits(0))