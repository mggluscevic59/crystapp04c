import logging

from pathlib import Path

PATH = ( Path | str )
_LOG = logging.getLogger(__name__)

def populate_map(path:PATH):
    rez = [Path("")]
    if isinstance(path, Path):
        rez = [path]
    elif isinstance(path, str):
        rez = [Path(path)]
    return rez

class Revisor:
    def __init__(self, path:PATH) -> None:
        self.path = path
        self.map = populate_map(path)
        self.log = _LOG
        self.log.debug("%s map: %s", __name__, self.map)
