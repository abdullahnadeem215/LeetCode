class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output = []
        for index, num in enumerate(nums):
            for i in range(index+1, len(nums)):
                if num + nums[i]== target:
                    output.append(index)
                    output.append(i)
                    return output