class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        change all 0's to -1
        find all sums that are the same

        p_sums[j] - p_sums[i-1] = 0
        p_sums[j] = p_sums[i-1]
        """
        max_len = 0

        p_sums = {0:[-1]}
        x = 0

        for i, num in enumerate(nums):
            if num == 0:
                x -= 1
            else:
                x += 1
            
            if x not in p_sums:
                p_sums[x] = [i]
            else:
                max_len = max(max_len, i - p_sums[x][0])
                p_sums[x].append(i)

        return max_len

            
            

            
