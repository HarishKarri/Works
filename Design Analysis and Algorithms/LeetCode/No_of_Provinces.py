# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

class Solution:
    def findCircleNum(self, isConnected):
        
        dictt = defaultdict(list)
        visited = []
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if(isConnected[i][j] == 1):
                    dictt[i].append(j)
        count = 0
        
        def dfs(node,count):
            visited.append(node)
            for vertex in dictt[node]:
                if vertex not in visited:
                    dfs(vertex,count)
            count +=1
            
            return count
        
        for key,val in dictt.items():
            if key not in visited:
                count = dfs(key,count)
        return count