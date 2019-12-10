# _*_coding:utf-8 _*_
import pandas as pd
import numpy as np


class baixi:

    def __init__(self):
        self.pd = pd
        self.deal_data = pd.read_excel(r'C:\Users\daojia\Desktop\学习\deal_data_x.xlsx', sheet_name='Sheet2')
        self.main_data = pd.read_excel(r'C:\Users\daojia\Desktop\学习\main_table_x.xlsx', sheet_name='Sheet1')

    # @staticmethod
    # 获取第一步数据
    # 获取城市名称
    def get_city_data(self):
        data = self.deal_data
        # a = data.columns[3:]
        city_data = [column for column in data]
        return city_data

    # 处理获取需要填充数据
    def get_first_data(self):
        city_data = self.get_city_data()[3:]
        deal_data = self.deal_data
        print(city_data)

        # first_data_1 = self.pd.read_excel(r'C:\Users\daojia\Desktop\学习\deal_data.xlsx', sheet_name='Sheet1')
        # 城市行转列
        first_data_2 = self.pd.melt(deal_data, id_vars=['date', 'hour', 'type'], value_vars=city_data,
                                    var_name='city', value_name='count_clue').fillna(0)

        first_data_2['count_clue'] = self.pd.to_numeric(first_data_2['count_clue'], errors='coerce')
        # first_data_2['count_clues'] = first_data_2['count_clue'].isnull().any()

        first_data_3 = self.pd.DataFrame(
            self.pd.pivot_table(first_data_2, index=['date', 'hour', 'city', ], columns='type', values='count_clue'))
        # 重置索引
        out_data = first_data_3.reset_index()
        out_data.to_excel(r'C:\Users\daojia\Desktop\学习\good123.xlsx')
        # data1 = data.stack()
        # print(out_data)
        # return out_data

    # 保存关系join相关数据
    # def save_join_data(self):
    #     first_data = self.get_first_data
    #     second_data = self.main_data
    #     out_data = self.pd.merge(second_data, first_data, on=['city', 'date'], how='left')
    #
    #     print(out_data)
    #     out_data.to_excel(r'C:\Users\daojia\Desktop\学习\good.xlsx')


if __name__ == '__main__':
    baixi().get_first_data()
    # baixi().get_city_data()
    a = 1
