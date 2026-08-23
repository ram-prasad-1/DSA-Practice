# 32. Alien Dictionary (premium) — topological sort over first differing characters
# Run: python 32_alien_dictionary.py
# Time: O(C) for C total characters. Space: O(1) — bounded by the alphabet.



from collections import deque



def alienOrder(words):
    graph = {c: set() for w in words for c in w}
    indeg = {c: 0 for c in graph}
    for a, b in zip(words, words[1:]):
        for x, y in zip(a, b):
            if x != y:
                if y not in graph[x]:
                    graph[x].add(y)
                    indeg[y] += 1
                break
        else:
            if len(a) > len(b):
                return ""
    q = deque(c for c in indeg if indeg[c] == 0)
    out = []
    while q:
        c = q.popleft()
        out.append(c)
        for nxt in graph[c]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)
    return "".join(out) if len(out) == len(indeg) else ""



print(alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))
print(repr(alienOrder(["abc", "ab"])))
