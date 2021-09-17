# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left_maxList,right_maxList = [0] * len(height),[0] * len(height)
        count = 0
        left_maxList[0] = height[0]
        right_maxList[-1] = height[-1]
        
        for i in range(1,len(height)):
            left_maxList[i] = max(left_maxList[i-1],height[i])
        
        
        for j in range(len(height)-2,-1,-1):
            right_maxList[j] = max(right_maxList[j+1],height[j])
            
        print(left_maxList)
        print(right_maxList)
        
        for i in range(1, len(height)-1):
            count += min(left_maxList[i],right_maxList[i]) - height[i]
        return count
            
            