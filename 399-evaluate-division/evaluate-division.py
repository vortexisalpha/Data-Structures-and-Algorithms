class Solution:
    def dfs(self, eq_dict, source, destination, cur_weight):
        if source in self.visited:
            return -1

        self.visited.add(source)
        if source == destination:
            return cur_weight
        max_dfs = -1
        for key, val in eq_dict[source].items():
            max_dfs = max(self.dfs(eq_dict, key, destination, cur_weight * val), max_dfs)
        return max_dfs
        


    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        eq_dict = {}
        for i in range(len(equations)):
            if equations[i][0] not in eq_dict:
                eq_dict[equations[i][0]] = {}
            if equations[i][1] not in eq_dict:
                eq_dict[equations[i][1]] = {}
            eq_dict[equations[i][0]][equations[i][1]] =  values[i]
            eq_dict[equations[i][1]][equations[i][0]] =  1/values[i]
        print(eq_dict)
        ans = []
        for query in queries:
            if query[0] == query[1] and query[0] in eq_dict:
                ans.append(1.0)
                continue
            
            
            if query[0] not in eq_dict or query[1] not in eq_dict:
                ans.append(-1.0)
                continue

            if query[0] in eq_dict and query[1] in eq_dict[query[0]]:
                ans.append(eq_dict[query[0]][query[1]])
                continue
            elif query[1] in eq_dict and query[0] in eq_dict[query[1]]:
                ans.append(eq_dict[query[1]][query[0]])
                continue

            self.visited = set()
            ans.append(self.dfs(eq_dict, query[0], query[1], 1))

        return ans

