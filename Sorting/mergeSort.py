# -*- coding: UTF-8 -*-


def merge(l1,l2,arr):
    i = j = 0
    while i+j<len(arr):
        if j==len(l2) or (i<len(l1) and l1[i] < l2[j]):
            # 如果第二个表走完了，或者第一个表没走完且l1[i] < l2[j]
            # 则表示还得比较两个表，且l1[i]比l2[j]更小，则新加入arr的元素为l1[i]
            
            arr[i+j] = l1[i]
            i += 1
        else:   # l1走完了或者都没走完l2[j]<l1[i] 则添加l2[j]到arr
            arr[i+j] = l2[j]

            j += 1
    
    pass

def mergeSort(arr):
    n = len(arr)
    if n < 2:
        return
    mid = n // 2
    l1 = arr[0:mid]
    l2 = arr[mid:n]
    mergeSort(l1)
    mergeSort(l2)
    merge(l1,l2,arr)
    
