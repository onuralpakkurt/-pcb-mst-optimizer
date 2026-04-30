from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import graph_routes, mst_routes

app = FastAPI(
    title="PCB MST Optimizer API",
    description=(
        "Backend service for the PCB MST Optimizer project. "
        "Exposes endpoints to manage a graph (vertices/edges) and compute "
        "the Minimum Spanning Tree using Kruskal + Union-Find. "
        "Graph data structures are implemented from scratch."
    ),
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(graph_routes.router)
app.include_router(mst_routes.router)


@app.get("/", tags=["meta"])
async def root():
    return {
        "service": "PCB MST Optimizer Backend",
        "version": "0.1.0",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health", tags=["meta"])
async def health():
    return {"status": "ok", "service": "pcb-mst-backend"}
