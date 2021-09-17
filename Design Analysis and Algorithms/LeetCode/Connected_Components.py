# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

# Return the number of connected components in the graph.

 

# Example 1:


# Input: n = 5, edges = [[0,1],[1,2],[3,4]]
# Output: 2

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        
        graphDict = {}
        for i in range(n):
            graphDict[i] = []
                
        for i in edges:
            graphDict[i[0]].append(i[1])
            graphDict[i[1]].append(i[0])
        
        def connectedComponents(currentNode,count):
            visited.append(currentNode)
            
            if currentNode in graphDict:
                for node in graphDict[currentNode]:
                    if node not in visited:
                        connectedComponents(node,count)
                count +=1
                return count
            else:
                return
        
        count = 0
        visited = []
        for i,j in graphDict.items():
            if i not in visited:
                count = connectedComponents(i,count)
        return count