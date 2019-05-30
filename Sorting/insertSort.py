# -*- coding: UTF-8 -*-

def insertSort(arr):
    """
    :param arr:接收一个列表作为变量，并对其进行排序
    :return: 无返回值
    思想：
        1. 默认第一个数为有序的
        2. 从第二个数将其插入到有序数组中的恰当位置
    """
    n = len(arr)
    for i in range(1,n):            # 默认第一个数有序，从第二个数开始遍历整个数组
        
        if arr[i] <= arr[i-1]:       # 如果未排序中第一个数比已排序最后一个数小，才需要将其排序
            tmp = arr[i]
            j = i-1
            while j>=0 and tmp < arr[j]:        # 从已排序最后往前遍历到0为止，如果d大于tmp则后移
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = tmp                      # 跳出循环则说明arr[j] >= tmp,则只需将tmp放在j的后面位置，即j+1处
