
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

def explore(graph, visited, node):
    #already seen
    if node in visited:
        return False

    #add to seen
    visited.add(node)

    #iterate over neighbors
    for neighbor in graph[node]:
        explore(graph, visited, neighbor)

    return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #turn list of edges into adjacency list
        graph = buildGraph(edges)
        
        #visited hashset
        visited = set()
        
        #keep track of count
        count = 0
        
        #iterate over nodes in graph
        for node in graph:
            if explore(graph, visited, node):
                count += 1
                
        #unlisted nodes
        count += n-len(visited) 
        
        return count 
        
        
        