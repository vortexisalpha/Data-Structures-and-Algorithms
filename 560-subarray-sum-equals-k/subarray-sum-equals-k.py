class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_hash = {0:1}
        prefix_sum = 0
        answer = 0
        for num in nums:
            prefix_sum += num
            answer += prefix_hash.get(prefix_sum - k, 0)
            if prefix_sum not in prefix_hash:
                prefix_hash[prefix_sum] = 1
            else:
                prefix_hash[prefix_sum] += 1 
            
        return answer