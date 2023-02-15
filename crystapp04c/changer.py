import logging

from pathlib import Path
from crystapp04c.constants import HEADER

INTEGRATION = None
CONCENTRATION = None

class Changer:
    def __init__(self, path) -> None:
        self.files = self.path_to_list(path)
        self._log = logging.getLogger(__name__)

    def path_to_list(self, new_path) -> list[Path]:
        path = Path(new_path)
        # is CSV
        if path.suffix == ".csv":
            return [path]
        elif path.is_dir():
            return [child for child in path.iterdir()]
        raise FileNotFoundError("File is not csv nor directory")

    def validate_csv_header(self):
        result = []
        for child in self.files:
            if not (child.suffix == ".csv"):
                # self._log.debug("%s skipped, not a csv", child.name)
                result.append(None)
            else:
                with child.open() as file:
                    header = file.readline()
                    # self._log.debug("%s", header)
                    if header.startswith(HEADER):
                        result.append(True)
                    else:
                        result.append(False)
        return result

    def add_constants_to_columns(self):
        pass

    def get_first_valid_csv(self):
        validation = self.validate_csv_header()
        for i in range(len(self.files)):
            if validation[i]:
                return self.files[i]
