class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        hashmap={}
        s=""
        n=len(words)
        for i in range(26):
            hashmap[i]=chr(ord('z')-i)
        for i in range(n):
            count=0
            for j in range(len(words[i])):
                currword=ord(words[i][j])-ord("a")
                count+=weights[currword]
            curr=count%26
            s+=hashmap[curr]
        return s