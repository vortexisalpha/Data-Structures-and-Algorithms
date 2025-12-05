
class Solution:
    #return the minimum time sum for separating the balloons
    # b b b 
    # 1 2 1

    def minCost(self, colors: str, neededTime: List[int]) -> int:
        start = 0
        end = 1
        ans = 0
        self.neededTime = neededTime
        while(start < len(neededTime) and end < len(neededTime)):
            max_time = 0
            if (end < len(neededTime) and colors[start] == colors[end]):
                max_time = neededTime[start]
                ans += neededTime[start]

            while(end < len(neededTime) and colors[start] == colors[end]):
                ans+= neededTime[end]
                max_time = max(max_time, neededTime[end])
                end+=1

            ans -= max_time
            start = end
            end+=1
         
        return ans