import logging

from pathlib import Path
from crystapp04c.constants import HEADER

INTEGRATION = 1
CONCENTRATION = 1

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
                with child.open(mode="r") as file:
                    header = file.readline()
                    # self._log.debug("%s", header)
                    if header.startswith(HEADER):
                        result.append(True)
                    else:
                        result.append(False)
        return result

    def add_constants_to_columns(self):
        validation = self.validate_csv_header()
        for i in range(len(self.files)):
            pass
            # valid csv file & constants not null
            if validation[i] and INTEGRATION and CONCENTRATION:
                with self.files[i].open(mode="r") as file:
                    all_lines = file.readlines()
                with self.files[i].open(mode="w") as file:
                    for index, line in enumerate(all_lines):
                        enlisted = line.split(",")
                        # write first line a description
                        if index == 0:
                            enlisted.insert(0, "integration")
                            enlisted.insert(2, "concetration")
                        else:
                            enlisted.insert(0, str(INTEGRATION))
                            enlisted.insert(2, str(CONCENTRATION))
                        line = ",".join(enlisted)
                        self._log.debug(line)
                        file.writelines(line)

    def get_first_valid_csv(self):
        validation = self.validate_csv_header()
        for i in range(len(self.files)):
            if validation[i]:
                return self.files[i]
