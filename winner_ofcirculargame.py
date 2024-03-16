class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        i=1
        Lst=[]
        while i<n+1:
            Lst.append(i)
            i+=1
        curindex=0
        while True:
            if len(Lst)==1:
                break
            i=(curindex+k-1)%len(Lst)
            Lst.remove(Lst[i])
            curindex=i%len(Lst)
        return Lst[0]