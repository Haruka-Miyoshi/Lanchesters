import numpy as np

# ランチェスターの法則（戦略）
class Lanchesters(object):
    # コンストラクタ
    def __init__(self, x0, y0, cx, cy):
        # x軍の戦力数の初期値
        self.x0 = x0
        # y軍の戦力数の初期値
        self.y0 = y0
        # x軍の武器性能
        self.cx = cx
        # y軍の武器性能
        self.cy = cy
        # 武器性能比
        self.R=self.cy / self.cx

    #### 1次元法則 ####
    # xに関する1次法則
    def linear_law_x(self, time):
        return self.x0 - self.cy * time
    
    # yに関する1次法則
    def linear_law_y(self, time):
        return self.y0 - self.cx * time
    
    # 武器の性能比率
    def linear_law_ratio(self):
        return self.R
    ###################

    #### 2次元法則 ####
    # xに関する1次元法則
    def linear2d_law_x(self, time):
        cxy=self.cx*self.cy
        return 0.5*( (self.x0 + np.sqrt(self.R)*self.y0)*np.exp(-np.sqrt(cxy)*time) + (self.x0 - np.sqrt(self.R)*self.y0)*np.exp(-np.sqrt(cxy)*time) )
    # yに関する2次元法則
    def linear2d_law_y(self, time):
        cxy=self.cx*self.cy
        return (0.5/np.sqrt(self.R))*( (self.x0 + np.sqrt(self.R)*self.y0)*np.exp(-np.sqrt(cxy)*time) - (self.x0 - np.sqrt(self.R)*self.y0)*np.exp(-np.sqrt(cxy)*time) ) 