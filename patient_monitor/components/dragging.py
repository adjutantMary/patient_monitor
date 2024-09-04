import reflex as rx
import random
from collections import defaultdict
from typing import Any, Dict, List


initial_nodes = [
    {
        'id': '1',
        'type': 'input',
        'data': {'label': '150'},
        'position': {'x': 250, 'y': 25},
    },
    {
        'id': '2',
        'data': {'label': '25'},
        'position': {'x': 100, 'y': 125},
    },
    {
        'id': '3',
        'type': 'output',
        'data': {'label': '5'},
        'position': {'x': 250, 'y': 250},
    },
]

initial_edges = [
    {'id': 'e1-2', 'source': '1', 'target': '2', 'label': '*', 'animated': True},
    {'id': 'e2-3', 'source': '2', 'target': '3', 'label': '+', 'animated': True},
]