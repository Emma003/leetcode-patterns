# def buildGraph(edges):
#     graph = {}
    
#     for a, b in edges:
        
#         if a not in graph:
#             graph[a] = []
#         if b not in graph:
#             graph[b] = []
            
#         graph[a].append(b)
#         graph[b].append(a)
        
#     return graph



# def hasPath(graph, src, dst, visited):
#     #found path
#     if src == dst:
#         return True
    
#     #already visited
#     if src in visited:
#         return False
    
#     #add to visited
#     visited[src] = True
    
#     #iterate over neighbors
#     for neighbor in graph[src]:
#         if hasPath(graph, neighbor, dst, visited):
#             return True
        
#     return False


def undirected_path(edges, node_A, node_B):
    graph = buildGraph(edges)
    visited = set()

    return dfs(graph, node_A, node_B, visited)
  
    
def dfs(graph, src, dst, visited):
    if src == dst:
        return True

    if src in visited:
        return False
    visited.add(src)


    for nei in graph[src]:
        if dfs(graph, nei, dst, visited):
            return True
    return False


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


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        #convert matrix to adjacency list
        graph = buildGraph(edges)
        
        # #find path
        # return hasPath(graph, source, destination, {})
        return dfs(graph, source, destination, set())