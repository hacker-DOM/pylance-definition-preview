from . import f     # docstrings correctly displayed on `f`
from src import f   # docstrings correctly displayed on `f`
from src.f import * # docstrings not displayed
import src.f        # docstrings not displayed