m, n = list(map(int, input().split()))
# m is number of translations of letters
# n is number of word pairs

d = dict()

def dfs(graph, start):
    visited = set()
    stack = [start]
    result = []
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            stack.extend(graph.get(node, []))
    
    return result
    

# definitions
for i in range(m):
    a, b = input().split()
    if a in d:
        d[a].add(b)
    else:
        d[a] = {b}

# translations
for i in range(n):
    source, dest = input().split()
    wrong = False

    # go through each letter
    for j in range(len(source)):
        if dest not in dfs(d, source):
            wrong = True
            break

    if wrong:
        print("no")
    else:
        print("yes")
