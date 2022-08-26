def buildGraph(edges):
    graph = {}
    
    for a, b in edges:
        
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
            
        graph[a].append(b)
        graph[b].append(a)
        
    return graph


def hasPath(graph, src, dst, visited):
    #found path
    if src == dst:
        return True
    
    #already visited
    if src in visited:
        return False
    
    #add to visited
    visited[src] = True
    
    #iterate over neighbors
    for neighbor in graph[src]:
        if hasPath(graph, neighbor, dst, visited):
            return True
        
    return False


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        #convert matrix to adjacency list
        graph = buildGraph(edges)
        
        #find path
        return hasPath(graph, source, destination, {})