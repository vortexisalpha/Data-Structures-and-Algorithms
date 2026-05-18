from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        #sum i to j = p_sum[j] - p_sum[i-1] (p_sum[-1] = 0)
        # p_sum[j] - p_sum[i-1] = k * integer
        # p_sum[j] - k * integer = p_sum[i-1]
        # the above equation is just mod(p_sum[j]) == mod(p_sum[i-1])

        mod_counter = {}
        mod_counter[0] = 1
        x = 0
        ans = 0
        for num in nums:
            x += num
            if x % k not in mod_counter:
                mod_counter[x % k] = 1
            else:
                ans += mod_counter[x % k]
                mod_counter[x % k] += 1
            
        return ans 