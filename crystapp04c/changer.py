from pathlib import Path

class Changer:
    def __init__(self, path) -> None:
        self.files = self.path_to_list(path)
       
    def path_to_list(self, new_path) -> list[Path]:
        path = Path(new_path)
        # is CSV
        if path.suffix == ".csv":
            return [path]
        elif path.is_dir():
            return [child for child in path.iterdir()]
        raise FileNotFoundError("File is not csv nor directory")
