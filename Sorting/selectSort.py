# -*- coding: UTF-8 -*-


def selectSort(arr):
    """
    :param arr: 接收一个列表作为变量，并对其进行排序
    :return: 无返回值
    思想：
        1. 列表分为已排序和未排序两个部分
        2. 遍历未排序列表，找出最小值，并将其与未排序列表中第一个值交换
    """
    n = len(arr)
    for i in range(n-1):        # 从第0个数遍历到倒数第二个数，表示已排序的列表
        j = i+1
        min_num = arr[j]
        index = j
        while j<n:              # 从第i+1个数便利到末尾，表示在未排序数组中寻找一个最小值
            if arr[j] < min_num:
                min_num = arr[j]
                index = j
            j += 1
        arr[i],arr[index] = arr[index],arr[i]
