# _*_coding:utf-8 _*_
import pandas as pd
import numpy as np


class baixi:

    # 初始化
    def __init__(self):
        self.pd = pd
        self.deal_data = pd.read_excel(r'C:\Users\daojia\Desktop\学习\work\Sample_bx.xlsx', sheet_name='Sheet1')

    # 转置过程，将null 值全部删除，重建。很值得学习
    # 真是精华所在,巧妙令人叹为观之,看来还是要面向stockflow
    @staticmethod
    def squeeze_nan(x):
        original_columns = x.index.tolist()

        squeezed = x.dropna()
        squeezed.index = [original_columns[n] for n in range(squeezed.count())]

        return squeezed.reindex(original_columns, fill_value=np.nan)

    # 重新获取数据
    def get_lc_data(self):
        # 获取数据
        data = self.deal_data
        data[data.__eq__(0)] = np.nan
        # 调用函数左移数据
        out_data = data.apply(self.squeeze_nan, axis=1)
        # 保存数据
        print(data)
        out_data.to_excel(r'C:\Users\daojia\Desktop\学习\Sample_y.xlsx')

        # return out_data


if __name__ == '__main__':
    baixi().get_lc_data()
    a = 1
