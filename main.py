import logging

from crystapp04c.revisor import Revisor, is_csv, extend_csv

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    # 1 & 3 column inserted
    data = {
        "integration"   : 0.0,
        ""              : 0.0,
        "conc"          : 0.0
    }
    path = input("File/Folder: ")
    rev = Revisor(path, **data)
    for path in rev.map:
        if path.is_file and is_csv(path):
            print("found CSV file: ", path)
            for key in rev.values.keys():
                if len(key):
                    rev.values[key] = float(input(f"{key}: "))
                else:
                    continue
            extend_csv(path, rev.values)
            print("File extended. Move file to another folder when done.")
