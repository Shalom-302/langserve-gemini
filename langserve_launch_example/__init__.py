"""langserve_launch_example package."""
from importlib import metadata

from langserve_launch_example.chain import ask_question

try:
    __version__ = metadata.version(__package__)
except metadata.PackageNotFoundError:
    # Case where package metadata is not available.
    __version__ = ""

__all__ = [__version__, "ask_question"]
