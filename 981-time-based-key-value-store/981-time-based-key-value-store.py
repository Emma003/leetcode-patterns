class TimeMap:

    def __init__(self):
        #maps key to 2d array
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.timeMap[key]
        res = ""
        l,r = 0, len(arr)-1
        
        while l <= r:
            mid = (l+r) // 2
            
            if arr[mid][0] == timestamp:
                return arr[mid][1]
            elif arr[mid][0] < timestamp:
                res = arr[mid][1]
                l = mid + 1
            else:
                r = mid -1
                
        return res

#         arr = self.dic[key]
#         n = len(arr)
        
#         left = 0
#         right = n
        
#         while left < right:
#             mid = (left + right) / 2
#             if arr[mid][0] <= timestamp:
#                 left = mid + 1
#             elif arr[mid][0] > timestamp:
#                 right = mid
        
#         return "" if right == 0 else arr[right - 1][1]