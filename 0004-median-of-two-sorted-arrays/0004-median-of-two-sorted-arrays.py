class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        array = nums1 + nums2
        array = sorted(array)
        median = 0
        for i in range(len(array)):
            if len(array)%2 ==0:
                if i == (len(array)//2):
                    median = (array[i]+array[i-1])/2.0
            else:
                if i == (len(array)//2):
                    median = array[i]

        return median