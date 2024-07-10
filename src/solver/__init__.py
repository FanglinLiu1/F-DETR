"""Based on https://github.com/lyuwenyu/RT-DETR
"""

from .solver import BaseSolver
from .det_solver import DetSolver


from typing import Dict 

TASKS :Dict[str, BaseSolver] = {
    'detection': DetSolver,
}