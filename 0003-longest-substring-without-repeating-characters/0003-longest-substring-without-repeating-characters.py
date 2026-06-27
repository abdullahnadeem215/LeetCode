class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        string = []
        max_string = 0
        for ch in s:
            if ch in string:

                index = string.index(ch)

                string = string[index+1:]

            string.append(ch)
        
            max_string = max(max_string,len(string))
        return max_string
        