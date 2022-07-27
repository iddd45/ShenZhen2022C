import numpy as np
from itertools import product


class Lorry:
    # 初始化
    def __init__(self, station1, station2):
        # 只考虑第一辆车的过程，后面的车与第一辆车一致
        # 75辆车奔跑
        # station1: P->D 换电站, station2: D->P 换电站位置
        self.bet = 100  # 当前电池电量
        self.p = 20 - station2  # 当前位置
        self.t = 0  # 当前时间
        self.station1 = station1
        self.station2 = station2
        self.n_charge = 0  # 充电次数

    # 返回对象为字符串表达式
    def __str__(self):
        return "Lorry is at position {}, with battery {}, at time {}".format(self.p, self.bet, self.t)

    def move(self, dt):
        # 从P点出发
        # 0(P)____10(D)___20(P')
        # dt时间后的演化结果，按0.1s设置
        if 0 <= self.p < 10 or np.isclose(self.p, 0):
            # 空载
            # np.isclose(self.p, 0):
            # p->D
            self.bet -= 1 / 2 * dt  # 电池消耗
        elif 10 <= self.p < 20 or np.isclose(self.p, 10):
            # 满载
            # D->P
            self.bet -= 1 / 3 * dt  # 电池消耗
        if self.bet < 0 or np.isclose(self.bet, 0):
import numpy as np
from itertools import product


class Lorry:
    # 初始化
    # 一次跑75辆车
    def __init__(self, station1, station2):
        # 只考虑第一辆车的过程，后面的车与第一辆车一致
        # 75辆车奔跑
        # station1: P->D 换电站, station2: D->P 换电站位置
        self.bet = 100  # 当前电池电量
        self.p = 20 - station2  # 当前位置
        self.t = 0  # 当前时间
        self.station1 = station1
        self.station2 = station2
        self.n_charge = 0  # 充电次数
        self.n_mission = 0  # 完成任务次数

    # 返回对象为字符串表达式
    def __str__(self):
        return "Lorry is at position {:.1f}, charged {:d} times, \n with battery {}, at time {}".format(self.p, self.bet, self.t)

    def move(self, dt):
        # 从P点出发
        # 0(P)____10(D)___20(P')
        # dt时间后的演化结果，按0.1s设置
        if 0 <= self.p < 10 or np.isclose(self.p, 0):
            # 空载
            # np.isclose(self.p, 0):
            # p->D
            self.bet -= 1 / 2 * dt  # 电池消耗
        elif 10 <= self.p < 20 or np.isclose(self.p, 10):
            # 满载
            # D->P
            self.bet -= 1 / 3 * dt  # 电池消耗
        if self.bet < 0 or np.isclose(self.bet, 0):
            # 出现不可行解
            raise Exception('Lorry is out of battery')
        self.t = self.t + dt  # 时间变化
        self.p = (self.p + dt * 1) % 20  # 位置变化
        if np.isclose(self.p, 0):
            # 装卸货时间
            self.t += 1
        if np.isclose(self.p, 10):
            self.t += 1
            self.n_mission += 1   # 完成一次运货任务
        self.recharge()

    def recharge(self):
        # 电池消耗
        # 12.6存在可行解
        # 目标函数
        # np.isclose 判断两个浮点数是否相等
        if (np.isclose(self.p, self.station1)) and 10 <= self.bet <= 12.6:
            # 满载到达
            # 目标函数
            # 逐渐降低阈值，测试是否存在可行解
            self.bet = 100
            self.t += 2
            self.n_charge += 1
        if np.isclose(self.p, 20 - self.station2) and 10 <= self.bet <= 12.6:
            # 空载到达
            self.bet = 100
            # 50min平均到75辆车
            self.t += 2/3  # 考虑换电为2，考虑换电为2/3
            self.n_charge += 1


lorry = Lorry(7.0,2.0)
print("选址为(7.0,2.0)")
while lorry.t < (1000*60 - 0.1):
    lorry.move(dt=0.1)
print(lorry)

# np.arange(0, 10, 1): 起始为0， 终点为10， 步长为1
# 第二问
# for (sta1, sta2) in product(np.arange(0, 10, 1), np.arange(0, 10, 1)):
#     #  for sta1 in np.arrange(0.1, 10, 0.1):
#     #      sta2 = sta1
#     #  第一问
#     lorry = Lorry(station1=sta1, station2=sta2)
#     try:
#         # T取0.1min
#         for T in range(1000 * 60 * 10):
#             lorry.move(dt=0.1)
#         print('({:.1f},{:.1f}) worked with charge {:d} times'.format(sta1, sta2, lorry.n_charge))
#     except Exception as e:
#         print((sta1, sta2), e, end='\r')

