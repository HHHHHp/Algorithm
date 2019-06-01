# -*- coding: UTF-8 -*-


def merge(l1,l2,arr):
    i = j = 0
    while i+j<len(arr):
        if j==len(l2) or (i<len(l1) and l1[i] < l2[j]):
            arr[i+j] = l1[i]
            i += 1
        else:
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
    
