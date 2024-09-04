from reflex import Component, EventHandler, Var
from typing import Any, Dict, List, Union
from reflex.vars import Var


class ReactFlowLib(Component):
    """A component that wraps a react flow lib."""

    library = "reactflow"

    def _get_custom_code(self) -> str:
        return """import 'reactflow/dist/style.css';
        """
class ReactFlow(ReactFlowLib):
    tag = "ReactFlow"

    nodes: Var[List[Dict[str, Any]]]

    edges: Var[List[Dict[str, Any]]]

    fit_view: Var[bool]

    nodes_draggable: Var[bool]

    nodes_connectable: Var[bool]

    nodes_focusable: Var[bool]

    on_nodes_change: EventHandler[lambda e0: [e0]]

    on_connect: EventHandler[lambda e0: [e0]]
    
# class Background(ReactFlowLib):
#     tag = "Background"

#     color: Var[str]

#     gap: Var[int]

#     size: Var[int]

#     variant: Var[str]


# class Controls(ReactFlowLib):
#     tag = "Controls"


react_flow = ReactFlow.create
# background = Background.create
# controls = Controls.create