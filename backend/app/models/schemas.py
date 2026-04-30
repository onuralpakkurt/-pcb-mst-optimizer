from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


class NodeInput(BaseModel):
    id: str = Field(..., description="Unique node identifier (ASCII)")
    label: Optional[str] = Field(None, description="Optional human-readable label")


class EdgeInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    from_node: str = Field(..., alias="from")
    to_node: str = Field(..., alias="to")
    weight: float = Field(..., gt=0, description="Edge weight (must be positive)")


class EdgeOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    from_node: str = Field(..., alias="from")
    to_node: str = Field(..., alias="to")
    weight: float


class GraphResponse(BaseModel):
    vertices: List[str]
    edges: List[EdgeOutput]
    vertex_count: int
    edge_count: int


class MSTResponse(BaseModel):
    edges: List[EdgeOutput]
    total_cost: float
    edge_count: int
    is_complete: bool
    message: str


class ConnectedResponse(BaseModel):
    is_connected: bool
    algorithm: str
    visited_count: int
    total_vertices: int


class GraphCreateResponse(BaseModel):
    message: str
    vertex_count: int
    edge_count: int
