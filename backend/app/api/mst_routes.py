from fastapi import APIRouter, HTTPException

from app.algorithms.bfs import is_connected_bfs
from app.algorithms.dfs import is_connected_dfs
from app.algorithms.kruskal import kruskal
from app.models.schemas import ConnectedResponse, EdgeOutput, MSTResponse
from app.services.graph_service import graph_service

router = APIRouter(prefix="/api", tags=["mst"])


@router.get("/mst", response_model=MSTResponse)
async def compute_mst():
    g = graph_service.get_graph()

    if g.vertex_count() == 0:
        raise HTTPException(status_code=400, detail="Graph is empty")

    result = kruskal(g)
    edges = [
        EdgeOutput.model_validate({"from": u, "to": v, "weight": w})
        for u, v, w in result["edges"]
    ]

    if result["is_complete"]:
        message = "MST computed successfully"
    else:
        message = "Graph is disconnected; partial spanning forest returned"

    return MSTResponse(
        edges=edges,
        total_cost=result["total_cost"],
        edge_count=result["edge_count"],
        is_complete=result["is_complete"],
        message=message,
    )


@router.get("/graph/connected", response_model=ConnectedResponse)
async def is_connected(algorithm: str = "bfs"):
    if algorithm not in ("bfs", "dfs"):
        raise HTTPException(
            status_code=400, detail="algorithm must be 'bfs' or 'dfs'"
        )

    g = graph_service.get_graph()

    if algorithm == "dfs":
        result = is_connected_dfs(g)
    else:
        result = is_connected_bfs(g)

    return ConnectedResponse(
        is_connected=result["is_connected"],
        algorithm=algorithm,
        visited_count=result["visited_count"],
        total_vertices=result["total_vertices"],
    )
