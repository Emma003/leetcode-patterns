class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        #lowercase
        paragraph = paragraph.lower()
        
        #remove all punctuation
        for punc in "!?',;.":
            paragraph = paragraph.replace(punc, " ")
            
        #turn banned into set
        banned = set(banned)
        
        #make non banned words dict
        cleanWords = {}
        
        #iterate and keep track of max
        res = ""
        maxCount = 0
        
        words = paragraph.split(" ")
        for word in words:
            if word in banned:
                continue
            
            if word.isalpha():
                if word not in cleanWords:
                    cleanWords[word] = 1

                cleanWords[word] += 1

                if cleanWords[word] > maxCount:
                    maxCount = cleanWords[word]
                    res = word
                
                
        return res
            