class Solution(object):
    '''
    -> Fuerza bruta
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
    '''
    def twoSum(self, nums, target):
        h = {}
        for i, num in enumerate(nums):
            h[num] = i
        
        for i, num in enumerate(nums):
            deseado = target - num
            if deseado in h and h[deseado] != i:
                return i, h[deseado]


    def twoSum(self, nums, target): 
        hash = {}
        for i,n in enumerate(nums):
            diff = target - nums[i]
            if diff in hash:
                return [hash[diff], i]
            hash[n] = i