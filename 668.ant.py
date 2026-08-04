from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List


LAYERS: Dict[str, List[str]] = {
    "context": ["regional_tension", "cross_border_trade", "migration_flow"],
    "state": ["government", "military_command", "intelligence_service"],
    "institution": ["humanitarian_agency", "regional_block", "mediator"],
    "public": ["civil_society", "media", "diaspora_network"],
}

EDGES = [
    ("regional_tension", "government", "signal"),
    ("government", "military_command", "coordination"),
    ("military_command", "intelligence_service", "intelligence"),
    ("regional_tension", "humanitarian_agency", "pressure"),
    ("humanitarian_agency", "civil_society", "aid_delivery"),
    ("regional_block", "mediator", "diplomatic_support"),
    ("migration_flow", "diaspora_network", "community_link"),
]


def build_graph() -> Dict[str, List[Dict[str, str]]]:
    nodes: List[Dict[str, str]] = []
    for layer_name, node_names in LAYERS.items():
        for node_name in node_names:
            nodes.append({"id": node_name, "layer": layer_name})

    edges: List[Dict[str, str]] = []
    for source, target, relationship in EDGES:
        edges.append({"source": source, "target": target, "relationship": relationship})

    return {"nodes": nodes, "edges": edges}


def write_output(output_path: str | Path = "geopolitical_layers.json") -> Dict[str, List[Dict[str, str]]]:
    data = build_graph()
    output_file = Path(output_path)
    output_file.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return data


if __name__ == "__main__":
    result = write_output()
    print(json.dumps(result, indent=2))
