import collections

class Node:
    def __init__(self, data, neighbors=[]):
        self.data = data
        self.neighbors = neighbors

def has_path_bfs(root, dest):
    visit_next = collections.deque()
    visit_next.append(root)
    visited = {}

    while len(visit_next):
        node = visit_next.popleft()

        if node.data == dest.data:
            return True
        
        visited[node.data] = ""
        for child in node.neighbors:
            if child not in visited:
                visit_next.append(child)

    return False

def has_path_dfs(root, dest):
    visited = {}

    return rec_dfs(root, dest, visited)

def rec_dfs(root, dest, visited):
    if root is None:
        return
    if root.data == dest.data:
        return True
    visited[root.data] = ""
    for node in root.neighbors:
        if node not in visited:
            if rec_dfs(node, dest, visited):
                return True
    return False




if __name__ == '__main__':
    root = Node(10, [Node(5), 
                     Node(7, [Node(8), Node(9)]),
                     Node(2, [Node(3, [Node(4)])])])
    dest = Node(4)

    print("BFS: %s" % has_path_bfs(root, dest))
    print("BFS: %s" % has_path_bfs(root, Node(1)))

    print("DFS: %s" % has_path_dfs(root, dest))
    print("DFS: %s" % has_path_dfs(root, Node(5)))


