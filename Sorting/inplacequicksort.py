# -*- coding: UTF-8 -*-
ls = []
import random
ls = []
a = 0               # a为数组第一个数索引
b = len(ls)-1       # b为最后一个数索引

def inplace_quick_sort(arr,a,b):
    if a >= b:      # 如果a>=b，则递归终止
        return
    pivot = arr[b]      # 设置最后一个数为pivot
    left = a
    right = b-1
    while left<=right:  # 当左指针小于右指针
        while left <= right and arr[left] <= pivot:     # 左值小于等于pivot则右移
            left += 1
        while left <= right and arr[right] >= pivot:    # 右值大于等于pivot则左移    都加上等于是为了能够平均分配等于pivot的值
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right],arr[left]    # 找到大于pivot的左值和小于pivot的右值并交换
            left,right = left+1, right-1
        
    arr[left],arr[b] = arr[b],arr[left]
    inplace_quick_sort(arr,a,left-1)
    inplace_quick_sort(arr,left+1,b)
