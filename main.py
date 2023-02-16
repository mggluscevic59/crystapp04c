import logging

from crystapp04c.changer import Changer

# _log = logging.getLogger(__name__)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    data = {
        "integration" : 0.0,
        "concentration" : 0.0
    }
    for key, _ in data.items():
        data[key] = float(input(f"{key}: "))

    path = input("Folder: ")
    ch = Changer(
        path=path,
        t=data["integration"],
        c=data["concentration"]
    )
    logging.info("Otput: %s %s", ch.files, ch.validate_csv_header())
    ch.add_constants_to_columns()
