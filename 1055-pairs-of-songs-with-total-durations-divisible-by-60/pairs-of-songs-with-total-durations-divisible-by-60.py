from collections import defaultdict
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time_rem = defaultdict(int)
        for i, x in enumerate(time):
            time_rem[x % 60] += 1

        
        cnt = 0  
        for x in time:
            cnt += time_rem[(60 - (x%60)) % 60]
            if (60 - (x%60)) % 60 == 30 or (60 - (x%60)) % 60 == 0:
                cnt -= 1

            print(cnt)
        return int(cnt/2)

          




