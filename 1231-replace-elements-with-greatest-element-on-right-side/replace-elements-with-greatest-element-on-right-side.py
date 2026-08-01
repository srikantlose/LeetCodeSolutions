class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        currmax=arr[len(arr)-1]
        for i in range(len(arr)-1,-1,-1):
            if arr[i]<=currmax:
                arr[i]=currmax
            else:
                temp=arr[i]
                arr[i]=currmax
                currmax=temp
        arr[len(arr)-1]=-1
        return arr
            
        