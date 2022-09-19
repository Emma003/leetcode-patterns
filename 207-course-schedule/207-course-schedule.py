def buildGraph(edges, numCourses):
    graph = {i: [] for i in range(numCourses)}
    
    for a,b in edges:
        graph[a].append(b)
        
    return graph


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = buildGraph(prerequisites, numCourses)
        visited = set()

        def dfs(node):
            if node in visited:
                return False

            if graph[node] == []:
                return True
            
            visited.add(node)
            
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            visited.remove(node)
            graph[node] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
    
        