# %%
import numpy as np
import matplotlib.pyplot as plt

# ランチェスターの法則（戦略）
class Lanchesters:
    # コンストラクタ
    def __init__(self, x0, y0, cx, cy) -> None:
        self.x0 = x0
        self.y0 = y0
        self.cx = cx
        self.cy = cy

    # xに関する1次法則
    def linear_law_x(self, time):
        return self.x0 - self.cy * time
    
    # yに関する1次法則
    def linear_law_y(self, time):
        return self.y0 - self.cx * time
    
    # 武器の性能比率
    def linear_law_ratio(self):
        return self.cy / self.cx

# 実行文
if __name__ == '__main__':
    # x軍の初期人数
    x0 = 10
    # x軍の持つ武器で、何人倒せるかの統計的な平均値
    cx = 1.5
    # y軍の初期人数
    y0 = 30
    # y軍の持つ武器で、何人倒せるかの統計的な平均値
    cy = 1.0

    # 時間
    max_time = 5

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
        x_linear.append(lancher.linear_law_x(t))
        y_linear.append(lancher.linear_law_y(t))
    
    # 武器の性能比率
    R = lancher.linear_law_ratio()

    plt.plot(x_linear)
    plt.plot(y_linear)
    plt.show()


# %%
