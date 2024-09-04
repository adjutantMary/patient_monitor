import reflex as rx
from .dragging import initial_edges, initial_nodes
from collections import defaultdict
from typing import Any, Dict, List



class State(rx.State):
    """The app state."""
    nodes: List[Dict[str, Any]] = initial_nodes
    edges: List[Dict[str, Any]] = initial_edges

    # def add_random_node(self):
    #     new_node_id = f"\{len(self.nodes) + 1}"
    #     node_type = random.choice(['default'])
    #     # Label is random number
    #     label = new_node_id
    #     x = random.randint(0, 500)
    #     y = random.randint(0, 500)

    #     new_node = {
    #         'id': new_node_id,
    #         'type': node_type,
    #         'data': {'label': label},
    #         'position': {'x': x, 'y': y},
    #         'draggable': True,
    #     }
    #     self.nodes.append(new_node)

    def clear_graph(self):
        self.nodes = []  # Clear the nodes list
        self.edges = []  # Clear the edges list

    # def on_connect(self, new_edge):
    #     # Iterate over the existing edges
    #     for i, edge in enumerate(self.edges):
    #         # If we find an edge with the same ID as the new edge
    #         if edge["id"] == f"e\{new_edge['source']}-\{new_edge['target']}":
    #             # Delete the existing edge
    #             del self.edges[i]
    #             break

        # Add the new edge
        # self.edges.append({
        #     "id": f"e\{new_edge['source']}-\{new_edge['target']}",
        #     "source": new_edge["source"],
        #     "target": new_edge["target"],
        #     "label": random.choice(["+", "-", "*", "/"]),
        #     "animated": True,
        # })

    def on_nodes_change(self, node_changes: List[Dict[str, Any]]):
        # Receives a list of Nodes in case of events like dragging
        map_id_to_new_position = defaultdict(dict)

        # Loop over the changes and store the new position
        for change in node_changes:
            if change["type"] == "position" and change.get("dragging") == True:
                map_id_to_new_position[change["id"]] = change["position"]

        # Loop over the nodes and update the position
        for i, node in enumerate(self.nodes):
            if node["id"] in map_id_to_new_position:
                new_position = map_id_to_new_position[node["id"]]
                self.nodes[i]["position"] = new_position
