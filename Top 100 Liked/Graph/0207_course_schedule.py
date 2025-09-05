class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = defaultdict(list)
        for a, b in prerequisites:
            indegree[a] += 1
            adj[b].append(a)
        s = []
        for i, j in enumerate(indegree):
            if j == 0:
                s.append(i)
        while s:
            c = s.pop()
            numCourses -= 1
            for p in adj[c]:
                indegree[p] -= 1
                if indegree[p] == 0:
                    s.append(p)
        return numCourses == 0
