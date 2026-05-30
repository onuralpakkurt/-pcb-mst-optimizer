from app.data_structures import Graph, Queue


def bfs(graph: Graph, start) -> set:
    visited = set()
    queue = Queue()

    queue.enqueue(start)
    visited.add(start)

    while not queue.is_empty():
        current = queue.dequeue()
        for neighbor in graph.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)

    return visited


def is_connected_bfs(graph: Graph) -> dict:
    vertices = graph.get_all_vertices()
    if not vertices:
        return {"is_connected": True, "visited_count": 0, "total_vertices": 0}

    visited = bfs(graph, vertices[0])
    return {
        "is_connected": len(visited) == len(vertices),
        "visited_count": len(visited),
        "total_vertices": len(vertices),
    }
