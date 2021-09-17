# On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three instructions:

# "G": go straight 1 unit;
# "L": turn 90 degrees to the left;
# "R": turn 90 degrees to the right.
# The robot performs the instructions given in order, and repeats them forever.

# Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

 

# Example 1:

# Input: instructions = "GGLLGG"
# Output: true
# Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
# When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
# Example 2:

# Input: instructions = "GG"
# Output: false


class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        x = y = 0
        
        direction = 0
        values = [[0,1],[1,0],[0,-1],[-1,0]]
        
        for i in instructions:
            if(i == 'L'):
                direction = (direction + 3)%4
            elif(i == 'R'):
                direction = (direction + 1)%4
            else:
                x += values[direction][0]
                y += values[direction][1]
        
        return (x==0 and y==0) or direction != 0
            