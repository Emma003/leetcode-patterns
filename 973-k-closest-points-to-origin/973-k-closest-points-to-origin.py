
def distance(pt1, pt2):
    pt1X, pt1Y, pt2X, pt2Y = pt1[0], pt1[1], pt2[0], pt2[1]
    
    return ((pt1X - pt2X)**2) + ((pt1Y - pt2Y)**2)



class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        for point in points:
            dist = distance([0,0], point)
            point.insert(0, dist)
            
            
        heapq.heapify(points)
        
        res = []
        for i in range(k):
            closePoint = heapq.heappop(points)
            res.append([closePoint[1], closePoint[2]])
            
        return res