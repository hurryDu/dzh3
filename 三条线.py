import numpy as np
import matplotlib.pyplot as plt


def distance(A, B):
    di = np.sqrt((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2 + (A[2] - B[2]) ** 2)
    return di


def PSO_Mass(M, n):
    p = np.zeros(3)
    maxgen = 100  # 进化次数
    sizepop = 100  # 种群规模
    Dim = 1  # 维度
    c1 = 1.4
    c2 = 1.4
    Vmax = 0.01  # 速度
    Vmin = -0.01
    Xmax = 1  # 位置
    Xmin = 0
    w = 0.8
    record = np.zeros(maxgen)

    # 产生初始粒子和速度
    pop = np.zeros((sizepop, Dim))
    V = np.zeros((sizepop, Dim))
    fitness = np.zeros(sizepop)

    for i in range(sizepop):
        # 随机产生一个种群
        pop[i] = [(Xmax - Xmin) * np.random.rand() * 1 + Xmin, (Xmax - Xmin) * np.random.rand() * 1 + Xmin,
                  (Xmax - Xmin) * np.random.rand() * 1 + Xmin]
        # 初始种群
        V[i] = [(Vmax - Vmin) * np.random.rand() * 1 + Vmin, (Vmax - Vmin) * np.random.rand() * 1 + Vmin,
                (Vmax - Vmin) * np.random.rand() * 1 + Vmin]
        # 初始化速度
        T_Dis = 0
        for j in range(n):
            t = pop[i]
            T_Dis += distance(t, M[j])
        fitness[i] = T_Dis  # 计算适应度

    # 个体极值和群体极值
    bestfitness, bestindex = np.min(fitness), np.argmin(fitness)  # bestindex:全局最优粒子索引
    gbest = pop[bestindex]  # 全局最佳位置
    pbest = pop  # 个体最佳
    fitnesspbest = fitness  # 个体最佳适应度值
    fitnessgbest = bestfitness  # 全局最佳适应度值

    # 迭代寻优
    for i in range(maxgen):  # 代数更迭
        for j in range(sizepop):  # 遍历个体
            # 速度更新
            V[j] = w * V[j] + c1 * np.random.rand() * (pbest[j] - pop[j]) + c2 * np.random.rand() * (gbest - pop[j])
            # 速度边界处理
            V[j][V[j] > Vmax] = Vmax
            V[j][V[j] < Vmin] = Vmin

            # 种群更新
            pop[j] = pop[j] + V[j]
            # 位置边界处理
            pop[j][pop[j] > Xmax] = Xmax
            pop[j][pop[j] < Xmin] = Xmin

            # 适应度值更新
            T_Dis = 0
            for k in range(n):
                t = pop[j]
                T_Dis += distance(t, M[k])
            fitness[j] = T_Dis

        for j in range(sizepop):
            # 个体最优更新
            if fitness[j] < fitnesspbest[j]:
                pbest[j] = pop[j]
                fitnesspbest[j] = fitness[j]
            # 群体最优更新
            if fitness[j] < fitnessgbest:
                gbest = pop[j]
                fitnessgbest = fitness[j]
        record[i] = fitnessgbest
        print(f'{i}      最小距离之和：{fitnessgbest}')  # 输出结果

    p = gbest
    return p

if __name__ == '__main__':
    n = 15  # 线的个数
    m = 20  # 点的个数
    data1 = np.loadtxt('data1.txt')  # 第一条线
    data2 = np.loadtxt('data2.txt')  # 第二条线
    data3 = np.loadtxt('data3.txt')  # 第三条线
    M1 = []
    M2 = []
    M3 = []
    T1 = []
    T2 = []
    T3 = []

    for i in range(n):  # 导入线
        M1.append(data1[m * (i):m * (i + 1)])
        M2.append(data2[m * (i):m * (i + 1)])
        M3.append(data3[m * (i):m * (i + 1)])

    for j in range(m):  # 导入同一时刻的n个点用于集结
        T1_j = []
        T2_j = []
        T3_j = []
        for k in range(n):
            T1_j.append(data1[j + m * (k - 1), :])
            T2_j.append(data2[j + m * (k - 1), :])
            T3_j.append(data3[j + m * (k - 1), :])
        T1.append(T1_j)
        T2.append(T2_j)
        T3.append(T3_j)

    P1 = np.zeros((m, 3))
    P2 = np.zeros((m, 3))
    P3 = np.zeros((m, 3))

    for i in range(m):
        P1[i] = PSO_Mass(T1[i], n)
        P2[i] = PSO_Mass(T2[i], n)
        P3[i] = PSO_Mass(T3[i], n)

    fig = plt.figure(1)
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.set_zlim([0, 1])

    for i in range(n):
        ax.plot(M1[i][:, 0], M1[i][:, 1], M1[i][:, 2], '-o', color='b', markersize=5, markerfacecolor='#D9FFFF')
        ax.plot(M2[i][:, 0], M2[i][:, 1], M2[i][:, 2], '-o', color='m', markersize=5, markerfacecolor='#FFD5DA')
        ax.plot(M3[i][:, 0], M3[i][:, 1], M3[i][:, 2], '-o', color='g', markersize=5, markerfacecolor='#d1f5cd')

    ax.plot(P1[:, 0], P1[:, 1], P1[:, 2], '-o', color='k', markersize=10, markerfacecolor='#FFEA08')
    ax.plot(P2[:, 0], P2[:, 1], P2[:, 2], '-o', color='k', markersize=10, markerfacecolor='#FFEA08')
    ax.plot(P3[:, 0], P3[:, 1], P3[:, 2], '-o', color='k', markersize=10, markerfacecolor='#FFEA08')

    plt.legend(['', '', '', ''])
    plt.show()
