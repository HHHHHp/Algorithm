# -*- coding: UTF-8 -*-

def countSort(arr):
    """
    计数排序
    思路：空间换时间
    扫描整个数组，找出最大值和最小值max_num, min_num
    新建一个长度为max_num - min_num + 1的数组
    
    :param arr:  输入一个数组
    :return: 无返回值
    """
    max_num = find_max(arr)
    min_num = find_min(arr)
    length = max_num - min_num + 1              # 计算新列表的长度
    new_list = [0 for i in range(length)]       # 初始化一个长度为length的新列表，并使其值全为0
    for num in arr:                             # 扫描一次arr 并将其以min_num的差为索引在新列表中计数
        diff = num - min_num
        new_list[diff] += 1
    curr = min_num
    n = 0
    for i in new_list:                          # 将新列表中的计数读出，值得注意的是，新列表中存的值并不是数值，而是某个数出现的次数
        while i > 0:
            arr[n] = curr
            n += 1
            i -= 1
        curr += 1
        
    
def find_max(arr):
    """
    找最大值
    :param arr:
    :return:
    """
    max_num = arr[0]
    for i in arr:
        if i > max_num:
            max_num = i
    return max_num


def find_min(arr):
    """
    找最小值
    :param arr:
    :return:
    """
    min_num = arr[0]
    for i in arr:
        if i < min_num:
            min_num = i
    return min_num

