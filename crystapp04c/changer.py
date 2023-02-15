from pathlib import Path

class Changer:
    def __init__(self, path) -> None:
        self.path = Path(path)
        self.files = []
        if self.path.suffix == "csv":
            self.files = [self.path]
        elif self.path.is_dir():
            for child in self.path.iterdir():
                self.files.append(child)
        else:
            raise FileNotFoundError("File is not csv nor directory")
