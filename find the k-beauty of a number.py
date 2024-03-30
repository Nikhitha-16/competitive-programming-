class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        b=0
        for i in range(len(s)-k+1):
            x=int(s[i:i+k])
            if x!=0 and num%x == 0:
                b+=1
        return b