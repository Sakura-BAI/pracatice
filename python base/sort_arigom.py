import pandas as pd


class baixi:

    @staticmethod
    def select_sort(origin_items, comp=lambda x, y: x < y):
        """简单选择排序"""
        # 理一下逻辑完成这个简单的, 核心就是互相比较,然后选择
        print(origin_items)
        # 获取原来数组的长度
        items = origin_items
        # 循环数组的长度
        for i in range(len(items) - 1):
            min_index = i
            for j in range(i + 1, len(items)):
                if comp(items[j], items[min_index]):
                    min_index = j
            items[i], items[min_index] = items[min_index], items[i]
        return items

    def to_do(self):
        items = [10, 9, 8, 6, 2, 23, 54]
        len(items)
        a = self.select_sort(items)
        print(a)


if __name__ == '__main__':
    baixi().to_do()
