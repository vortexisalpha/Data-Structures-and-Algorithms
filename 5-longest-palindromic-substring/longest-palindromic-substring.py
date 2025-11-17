class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        def same(a,b):
            return a == b
        
        out = ""
        #odd
        for i in range(n):
            it1 = i
            it2 = i
            it3 = i
            it4 = i+1
            while (it1 >= 0 and it2 <= n-1):
                
                if not same(s[it1], s[it2]):
                    out = max(s[it1+1:it2], out, key=len)
                    break
                elif (it1 == 0 or it2 == n-1):
                    out = max(s[it1:it2+1], out, key=len)
                it1 -= 1
                it2 += 1

            if it4 < n and same(s[it3], s[it4]):
                while (it3 >= 0 and it4 <= n-1):
                    if not same(s[it3], s[it4]):
                        out = max(s[it3+1:it4], out, key=len)
                        break
                    elif (it3 == 0 or it4 == n-1):
                        out = max(s[it3:it4+1], out, key=len)
                    it3 -= 1
                    it4 += 1
                
        return max(out, s[0], key=len)
                
                    

        #even
