import tushare as ts


class test:
    '''
    测试获取数据，挺好用的这个接口。
    接下来就是数据分析来着。
    '''

    @staticmethod
    def get_hist_data():
        data = ts.get_hist_data('601398')
        data.to_excel(r'C:\Users\daojia\Desktop\工作\201911\601398.xlsx')
        print(data)
        return data


if __name__ == '__main__':
    test.get_hist_data()
    a = 1
