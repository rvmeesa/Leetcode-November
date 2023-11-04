class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        ans=0
        for i in range (len(left)):
            ans=max(ans,left[i])
        
        for i in range (len(right)):
            ans=max(ans,n-right[i])
        
        return ans