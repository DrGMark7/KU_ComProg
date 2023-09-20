class Solution:
    def convert(self, s: str, numRows: int) -> str:
        vPos = 0
        hPos = 0
        remaining = len(s)
        index = 0
        down = True
        res = []
        
        if numRows == 1:
            return s
        
        while remaining > 0:
            
            res.append((vPos, hPos, s[index]))
            
            if down and vPos < numRows-1:
                vPos += 1
            elif down and vPos == numRows-1:
                down = False
                vPos -= 1
                hPos += 1
            elif not down and vPos > 0:
                vPos -= 1
                hPos += 1
            elif not down and vPos == 0:
                down = True
                vPos += 1
            
            remaining -= 1
            index += 1
        
        res.sort()
        res = [j[2] for j in res]
        return "".join(res)
    
S = Solution()
s = str(input("Input sentence: "))
r = int(input("Input row: "))

print(S.convert(s,r))