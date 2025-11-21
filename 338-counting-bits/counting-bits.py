class Solution:
    
    def countBits(self, n: int) -> List[int]:
        arr=[]
        for i in range(0,n+1):
            x = i
            cnt = 0
            while(x > 0):
                cnt += x%2
                x //= 2

            arr.append(cnt)
        return arr