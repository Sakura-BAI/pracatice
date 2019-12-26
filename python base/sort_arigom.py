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
                # 发现数值大小之后,交换数值.通过交换索引来交换数值.好好学习.这个最基础的就好了.
                if comp(items[j], items[min_index]):
                    min_index = j
            items[i], items[min_index] = items[min_index], items[i]
        return items

    @staticmethod
    # 没有必要看,等有空了再学习冒泡排序,用不着.
    def bubble_sort(origin_items, comp=lambda x, y: x > y):
        """高质量冒泡排序(搅拌排序)"""
        items = origin_items[:]
        for i in range(len(items) - 1):
            swapped = False
            for j in range(i, len(items) - 1 - i):
                if comp(items[j], items[j + 1]):
                    items[j], items[j + 1] = items[j + 1], items[j]
                    swapped = True
            if swapped:
                swapped = False
                for j in range(len(items) - 2 - i, i, -1):
                    if comp(items[j - 1], items[j]):
                        items[j], items[j - 1] = items[j - 1], items[j]
                        swapped = True
            if not swapped:
                break
        return items

    @staticmethod
    def merge_sort(items, comp=lambda x, y: x <= y):

        """归并排序(分治法)"""
        if len(items) < 2:
            return items[:]
        mid = len(items) // 2
        left = merge_sort(items[:mid], comp)
        right = merge_sort(items[mid:], comp)
        return merge(left, right, comp)


    def to_do(self):
        items = [10, 9, 8, 6, 2, 23, 54]
        len(items)
        a = self.bubble_sort(items)
        print(a)


if __name__ == '__main__':
    baixi().to_do()
