class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        blocks=list(blocks)
        for i in range (len(blocks)):
            if blocks[i]=='W':
                blocks[i]=0
            else:
                blocks[i]=1
        print(blocks)
        if len(blocks)==1 and blocks[0]==0:
            return 1
        elif len(blocks)==1 and blocks[0]==1:
            return 0
        L,R=0,0
        minDiff=float('inf')
        add=0
        while R<len(blocks):
            add=add+blocks[R]
            
            if R-L+1==k:
                if add==k:return 0
                
                
                #R=L+1  
                minDiff=min(minDiff,k-add)
                add-=blocks[L]
                L+=1
                
            R+=1
        return minDiff