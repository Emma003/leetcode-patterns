class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        #first pass: move all digit logs to the back (two pointers)
        i = len(logs) - 1
        for j in range(len(logs)-1, -1, -1):
            currLog = logs[j]
            tokenSplit = currLog.split(" ")
            
            if tokenSplit[1].isnumeric():
                #swap i and j then move i inwards
                logs[i], logs[j] = logs[j], logs[i]
                i -= 1
                
        #make sorting function
        def compare(arr1, arr2):
            tokens1 = arr1.split(" ", 1)
            tokens2 = arr2.split(" ", 1)
            
            #same contents
            if tokens1[1] == tokens2[1]:
                #sort by identifiers
                if tokens1[0] < tokens2[0]:
                    return -1
                elif tokens2[0] < tokens1[0]:
                    return 1
                else:
                    return 0
                
            elif tokens1[1] < tokens2[1]:
                return -1
            else:
                return 1

            return compare

        sortedLetterLogs = sorted(logs[:i+1],key=cmp_to_key(compare))
        
        return sortedLetterLogs + logs[i+1:]

        