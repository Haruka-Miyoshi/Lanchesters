import os
import numpy as np
import matplotlib.pyplot as plt
from lanchesters import Lanchesters

if not os.path.exists('./figs'):
    os.mkdir('./figs')

def main():
    # x軍の初期人数
    x0 = 10
    # x軍の持つ武器で、何人倒せるかの統計的な平均値
    cx = 1.5
    # y軍の初期人数
    y0 = 30
    # y軍の持つ武器で、何人倒せるかの統計的な平均値
    cy = 1.0

    # 時間
    max_time = 10

    # ランチェスタークラス
    lancher = Lanchesters(x0, y0, cx, cy)

    # 時間
    time = [i for i in range(max_time)]

    # xに関する1次法則
    x_linear = []
    # yに関する1次法則
    y_linear = []
    
    # 一定時間で実行
    for t in range(max_time):
        x_linear.append(lancher.linear2d_law_x(t))
        y_linear.append(lancher.linear2d_law_y(t))
    
    # 武器の性能比率
    R = lancher.linear_law_ratio()
    plt.xlim(min(time), max(time))
    plt.title('Lanchesters2D')
    plt.ylabel('Force Count')
    plt.xlabel('time')
    plt.plot(x_linear, c='r', label='X Force')
    plt.plot(y_linear, c='b', label='Y Force')
    plt.legend()
    plt.savefig('./figs/Lanchesters2D.png')
    plt.show()

# 実行文
if __name__ == '__main__':
    main()