'''
题目：港口卸货
港口的卸货机制：若干艘船都装有6个集装箱，num个起重机，每个起重机每单位时间可完成一个集装箱的卸货；
各货轮到达时间记录于数组time;
t+limit时刻前无法完成所有集装箱的卸货，该货轮无需卸货，直接进入等候区；
问有多少艘货轮需要进入等候区；

示例：
输入：
num = 20
time = [3, 3, 5, 5, 5, 5, 5, 5]
limit = 2

输出：
0

输入：
num = 5
time = [1, 2, 2, 3, 3, 4, 5, 5]
limit = 3

输出：
3
'''

# 解法：双重for循环暴力解法；
# 外层for循环：每个起重机每单位时间可完成一个集装箱的卸货------ 每过一个单位时间，卸走num个货物, 有货且大于等于num个货物的情况下；
#    内层for循环：time -------- 各时间点来的货物，并做出是否进入等候区的决策；

from typing import List
import math

class Solution:
    def get_manual_unloading_num(self, num: int, time: List[int], limit: int)-> int:
        hasgoods = 0
        res = 0
        for timenow in range(1, max(time) + 1):
            for timecur in time:
                if timenow == timecur:
                    hasgoods += 6
                    if math.ceil(hasgoods / num) > limit:
                        res += 1
                        hasgoods -= 6
            hasgoods = max(hasgoods - num, 0)
        return res

if __name__ == '__main__':
    num = 5
    time = [1, 2, 2, 3, 3, 4, 5, 5]
    limit = 3
    solution = Solution()
    print(solution.get_manual_unloading_num(num, time, limit))




