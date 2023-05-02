from collections import defaultdict
from copy import deepcopy

'''
Shortest path algorithms. Shortest path almost always means that you should do some kind of BFS. However, I will also
add some DFS. 
'''

'''
Data structure undirected weighted graph
graph = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]

Going from node1 to node2 costs 9 and vice versa
Going from node2 to node3 costs 6 and vice versa
etc...

'''

nodes = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]


def create_undirected_weighted_graph(nodes):
    graph = defaultdict(list)
    for s, d, w in nodes:
        graph[s].append((d, w))
        graph[d].append((s, w))
    return graph


def create_directed_weighted_graph(ni):
    graph = defaultdict(list)
    for s, d, w in nodes:
        graph[s].append((d, w))
    return graph


'''
Find shortest path undirected graphs using DFS 
'''


def find_shortest_dfs(nodes, dest=4):
    graph = create_undirected_weighted_graph(nodes)
    print(graph)
    global ans
    ans = float("inf")

    # Explore all paths
    def dfs(node, c, visited):
        global ans
        if node == dest:
            ans = min(ans, c)
            return
        for n, w in graph[node]:
            if (n, w) not in visited:
                visited = deepcopy(visited)
                visited.add((n, w))
                dfs(n, c + w, visited)

    dfs(1, 0, set())
    return ans





if __name__ == "__main__":
    ans = find_shortest_dfs(nodes, 4)
    print(ans)
    # graph = create_undirected_weighted_graph(nodes)
    # print(graph)
