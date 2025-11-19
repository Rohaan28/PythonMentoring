# 2154. Keep Multiplying Found Values by Two
class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        nums=sorted(nums)
        for n in nums:
            if n == original:
                original = original*2
        print("%d is not found " % original)
        return original
    

# 268. Missing Number
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for x in range(len(nums)+1):
            if x not in nums:
                return x
            
# 349. Intersection of Two Arrays
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for n in nums1:
            if n in nums2 and n not in output:
                output.append(n)
        return output
        