class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        windowSize = len(s)
        while windowSize > 1:
            slidingWindowCount = len(s)-windowSize + 1
            index = 0
            while slidingWindowCount > 0:
                mp = {}
                tmpstr = s[index:windowSize+index]
                for i in tmpstr:
                    if i not in mp:
                        j = i.swapcase()
                        if j in mp:
                            mp[j] = 2
                        else:
                            mp[i] = 1
                for i, j in mp.items():
                    if j == 1:
                        break
                else:
                    return tmpstr
                index+=1
                slidingWindowCount-=1
            windowSize-=1
        return ""