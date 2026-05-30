from app.data_structures import Graph, Stack


def dfs(graph: Graph, start) -> set:
    visited = set()
    stack = Stack()
    stack.push(start)

    while not stack.is_empty():
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        for neighbor in graph.get_neighbors(current):
            if neighbor not in visited:
                stack.push(neighbor)

    return visited


def is_connected_dfs(graph: Graph) -> dict:
    vertices = graph.get_all_vertices()
    if not vertices:
        return {"is_connected": True, "visited_count": 0, "total_vertices": 0}

    visited = dfs(graph, vertices[0])
    return {
        "is_connected": len(visited) == len(vertices),
        "visited_count": len(visited),
        "total_vertices": len(vertices),
    }
