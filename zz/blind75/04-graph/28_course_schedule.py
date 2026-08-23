# 28. Course Schedule — cycle detection via Kahn's topological sort
# Run: python 28_course_schedule.py
# Time: O(V + E). Space: O(V + E).



from collections import deque



def canFinish(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    indeg = [0] * numCourses
    for a, b in prerequisites:
        graph[b].append(a)
        indeg[a] += 1
    q = deque(i for i in range(numCourses) if indeg[i] == 0)
    done = 0
    while q:
        c = q.popleft()
        done += 1
        for nxt in graph[c]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)
    return done == numCourses



print(canFinish(2, [[1, 0]]))
print(canFinish(2, [[1, 0], [0, 1]]))
