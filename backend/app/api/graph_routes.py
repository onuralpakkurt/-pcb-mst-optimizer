from fastapi import APIRouter, HTTPException, status

from app.models.schemas import (
    EdgeInput,
    EdgeOutput,
    GraphCreateResponse,
    GraphResponse,
    NodeInput,
)
from app.services.graph_service import graph_service

router = APIRouter(prefix="/api/graph", tags=["graph"])


@router.post("", response_model=GraphCreateResponse, status_code=status.HTTP_201_CREATED)
async def create_graph():
    await graph_service.reset()
    return GraphCreateResponse(message="Graph created", vertex_count=0, edge_count=0)


@router.post("/node", status_code=status.HTTP_201_CREATED)
async def add_node(node: NodeInput):
    count = await graph_service.add_node(node.id)
    return {"id": node.id, "vertex_count": count}


@router.post("/edge", status_code=status.HTTP_201_CREATED)
async def add_edge(edge: EdgeInput):
    if edge.from_node == edge.to_node:
        raise HTTPException(
            status_code=400, detail="Self-loop not allowed (from == to)"
        )
    count = await graph_service.add_edge(edge.from_node, edge.to_node, edge.weight)
    return {
        "from": edge.from_node,
        "to": edge.to_node,
        "weight": edge.weight,
        "edge_count": count,
    }


@router.get("", response_model=GraphResponse)
async def get_graph():
    g = graph_service.get_graph()
    edges = [
        EdgeOutput.model_validate({"from": u, "to": v, "weight": w})
        for u, v, w in g.get_all_edges()
    ]
    return GraphResponse(
        vertices=g.get_all_vertices(),
        edges=edges,
        vertex_count=g.vertex_count(),
        edge_count=g.edge_count(),
    )
