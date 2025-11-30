from collections import defaultdict
class Solution:
    def not_all_none(self,adj_mat):
        for x in adj_mat:
            flag = False
            if len(x) == 0:
                flag = True
            if flag == False:
                return False
        return True

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_mat = [[]for _ in range(numCourses)]
        for x, y in prerequisites:
            adj_mat[x].append(y)
        #at least one has to be empty
        print(adj_mat)
        flag = False
        for x in adj_mat:
            if len(x) == 0:
                flag = True
        if flag == False:
            return []

        seen = []
        while(not self.not_all_none(adj_mat) or len(seen) != numCourses):
            empty_checker = -1
            for i,x in enumerate(adj_mat):
                if len(x) == 0 and i not in seen:
                    empty_checker = i
                    seen.append(i)
                    break
            if empty_checker == -1:
                return []

            for i in range(len(adj_mat)):
                for j in range(len(adj_mat[i])):
                    if empty_checker == adj_mat[i][j]:
                        adj_mat[i].pop(j)
                        break
            
            
        return list(seen)



        print(adj_mat)

        