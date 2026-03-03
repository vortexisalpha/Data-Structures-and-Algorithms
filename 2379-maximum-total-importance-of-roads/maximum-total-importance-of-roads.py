class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        mapping = {}
        for i in range(len(roads)):
            for j in range(2):
                if roads[i][j] in mapping:
                    mapping[roads[i][j]] += 1
                else:
                    mapping[roads[i][j]] = 1

        sorted_maps = list(zip(mapping.values(), mapping.keys()))
        sorted_maps = sorted(sorted_maps)
        score = 0
        idx = 0
        for i in range(len(sorted_maps)-1, -1,-1):
            score += (n-idx) * sorted_maps[i][0]
            idx += 1
        return score
            
