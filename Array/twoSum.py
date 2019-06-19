# -*- coding: UTF-8 -*-
# by Hp

"""
给定一个整数数组nums和一个目标target
返回两个索引，使其对应值的和为target
"""
array = [2,3,4,5,6,7]
target = 7

class Solution:
    def twoSum(self, nums, target):
        dic = {}
        for i in range(0,len(nums)):
            if dic.get(nums[i]):
                return [dic[nums[i]], i]
            else:
                need = target - nums[i]
                dic[need] = i
        
print(Solution().twoSum(array,target))