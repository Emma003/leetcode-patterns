
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #build graph 
        graph = {i: [] for i in range(numCourses)}
        for a,b in prerequisites:
            graph[a].append(b)
            
        visited = set()
        
        def dfs(node):
            if node in visited:
                return False
            
            if graph[node] == []:
                return True
            
            visited.add(node)
            
            for nei in graph[node]:
                if not dfs(nei):
                    return False
                
            #remove from the visited set after whole path is visited
            visited.remove(node)
            
            #set num of neighbors to zero (all neighbors were visited)
            graph[node] = []
            
            return True
            
        for crs in range(numCourses):
            if not dfs(crs):
                return False
            
        return True
        