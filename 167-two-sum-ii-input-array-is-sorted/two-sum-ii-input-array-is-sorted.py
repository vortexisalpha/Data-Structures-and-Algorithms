class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            
            left = i + 1
            right = len(numbers)-1
            while left <= right:
                mid = (left + right) // 2
                if numbers[i] + numbers[mid] == target:
                    return sorted([i + 1, mid + 1])
                elif numbers[i] + numbers[mid] > target:
                    right = mid -1
                elif numbers[i] + numbers[mid] < target:
                    left = mid + 1 
        return [0,0]