# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2
# Example 2:

# Input: intervals = [[7,10],[2,4]]
# Output: 1

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        
        sortedList = sorted(intervals, key = lambda x:x[0])
        
        result = [sortedList[0]]
        
        
        for index in range(1,len(sortedList)):
            currentstart = sortedList[index][0]
            currentend = sortedList[index][1]
            flag = False
            for i in range(len(result)):
                if(result[i][0] <= currentstart < result[i][1]):
                    flag = True
                else:
                    result[i] = [result[i][0], max(currentend,result[i][1])]
                    flag= False
                    break;
            if(flag):
                result.append(sortedList[index])
        return len(result)
            