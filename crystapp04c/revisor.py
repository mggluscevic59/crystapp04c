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
    
    # map => list
    if rez[0].is_dir():
        i = []
        for child in rez[0].iterdir():
            i.append(child)
        return i
    return rez

class Revisor:
    def __init__(self, path:PATH) -> None:
        self.path = path
        self.map = populate_map(path)
        self.log = _LOG
        self.log.debug("%s map: %s", __name__, self.map)
