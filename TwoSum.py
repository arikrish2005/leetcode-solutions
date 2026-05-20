class Solution(object):
    def twoSum(self, nums, target):
        hashmap={}
        for i in range(len(nums)):
            num = nums[i]
            num2=target-num
            if num2 in hashmap:
                return [hashmap[num2], i]
            hashmap[num]=i
