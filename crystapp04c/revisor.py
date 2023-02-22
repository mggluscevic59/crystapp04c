import logging
import csv
import pandas

from pathlib import Path

PATH = ( Path | str )
VALUES = dict[str, float]
_LOG = logging.getLogger(__name__)

def folder_map(path:PATH):
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

def is_file(path:PATH):
    rez = False

    if isinstance(path, Path):
        rez = path.is_file()
    elif isinstance(path, str):
        rez = Path(path).is_file()

    return rez

def is_csv(path:PATH):
    rez = False
    x = ""
    if isinstance(path, str):
        x = path
    else:
        x = str(path.absolute())
    if csv.Sniffer().has_header(sample=x):
        rez = True
    return rez

def extend_csv(path:PATH, values:VALUES):
    x = Path(path) if isinstance(path, str) else path
    file = pandas.read_csv(x.absolute())
    for index, key in enumerate(values.keys()):
        if len(key) != 0:
            # file[key.index] = [values[key] for _ in range(len(file))]
            file.insert(index, key, [values[key] for _ in range(len(file))])
    file.to_csv(x.absolute(), index=False)

class Revisor:
    def __init__(self, path:PATH, **args) -> None:
        self.parent = path
        self.map = folder_map(path)
        self.log = _LOG
        self.log.debug("%s map: %s", __name__, self.map)
        self.values:dict[str, float] = {}
        for key in args:
            self.values[key] = args[key]
        # for key, value in args:
        #     self.log.debug("%s args: %s", __name__, val)
