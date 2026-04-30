const API_BASE_URL = "http://localhost:8000";

export async function getGraph() {
  const response = await fetch(`${API_BASE_URL}/graph`);
  return response.json();
}

export async function calculateMst() {
  const response = await fetch(`${API_BASE_URL}/mst`, {
    method: "POST",
  });

  return response.json();
}

export async function addNode(nodeData) {
  const response = await fetch(`${API_BASE_URL}/nodes`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(nodeData),
  });

  return response.json();
}
