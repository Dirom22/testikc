graph = {'0': set(['1', '2']),
	'1': set(['0', '3', '4']),
	'2': set(['0']),
	'3': set(['1']),
	'4': set(['2', '3'])}

visited = []
queue = []

def bfs(visited, graph, node):
    global queue
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0)
        print (s, end = " ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print(bfs(visited, graph, '2'))