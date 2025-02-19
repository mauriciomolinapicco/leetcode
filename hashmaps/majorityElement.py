class Solution(object):
    def majorityElement(self, nums):
        hash_map = {}
        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 0
        return max(hash_map, key=hash_map.get)