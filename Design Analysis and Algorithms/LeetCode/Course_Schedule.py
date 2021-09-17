# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        self.courseDict = {i:[] for i in range(numCourses)}
        
        for courses in prerequisites:
            self.courseDict[courses[0]].append(courses[1])
        # print(self.courseDict)
        self.visited = []
        for course in range(numCourses):
            # print(course)
            if(self.dfs(course) is False):
                return False
        return True
    
    def dfs(self,course):
        if course in self.visited:
            return False
        
        if self.courseDict[course] == []:
            return True
        else:
            self.visited.append(course)
            # print(self.visited)
            for subcourses in self.courseDict[course]:
                if(self.dfs(subcourses) is False):
                    return False
            self.visited.pop()
            self.courseDict[course] = []
            return True
        
        
        