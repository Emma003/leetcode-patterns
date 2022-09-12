

class Solution:
    def canFinish(self, tasks: int, prerequisites: List[List[int]]) -> bool:
        sortedOrder = []
        if tasks <= 0:
            return False

        # a. Initialize the graph
        inDegree = {i: 0 for i in range(tasks)}  # count of incoming edges
        graph = {i: [] for i in range(tasks)}  # adjacency list graph

        # b. Build the graph
        for prerequisite in prerequisites:
            parent, child = prerequisite[0], prerequisite[1]
            graph[parent].append(child)  # put the child into it's parent's list
            inDegree[child] += 1  # increment child's inDegree

        # c. Find all sources i.e., all vertices with 0 in-degrees
        sources = deque()
        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)

        # d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
        # if a child's in-degree becomes zero, add it to the sources queue
        while sources:
            vertex = sources.popleft()
            sortedOrder.append(vertex)
            for child in graph[vertex]:  # get the node's children to decrement their in-degrees
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)

        # if sortedOrder doesn't contain all tasks, there is a cyclic dependency between tasks, therefore, we
        # will not be able to schedule all tasks
        return len(sortedOrder) == tasks

        
        
#         #if only one course
#         if numCourses < 2:
#             return True
        
#         #build graph + keep track of inDegrees
#         graph = {}
#         inDeg = {}
        
#         for a,b in prerequisites:
#             if a not in graph:
#                 graph[a] = []
#             if a not in inDeg:
#                 inDeg[a] = 0
             
#             if b not in graph:
#                 graph[b] = []
#             if b not in inDeg:
#                 inDeg[b] = 0
                
#             graph[a].append(b)
#             graph[b].append(a)
            
#             #increment inDeg of b (b is at receivend end of arrow)
#             inDeg[b] += 1
            
        
        
#         #add sources to a deque (the nodes with inDeg == 0)
#         sources = deque()
#         for node in inDeg:
#             if inDeg[node] == 0:
#                 sources.append(node)
        
        
#         #while deque, pop sources and append to sorted list
#         sortedCourses = []
#         while sources:
#             curr = sources.popleft()
#             sortedCourses.append(curr)
            
#             #iterate over neighbors and add to neighbors if inDeg == 0
#             for neighbor in graph[curr]:
#                 inDeg[neighbor] -= 1
#                 if inDeg[neighbor] == 0:
#                     sources.append(neighbor)
        
        
        
#         #if len(deque) == numCourses, return True
#         return len(sortedCourses) == numCourses