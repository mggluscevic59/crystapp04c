import logging

from crystapp04c.changer import Changer

# _log = logging.getLogger(__name__)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    data = {
        "integration" : 3,
        "concentration" : 3
    }
    for key, _ in data.items():
        data[key] = int(input(f"{key}: "))

    path = input("Folder: ")
    ch = Changer(
        path=path,
        t=data["integration"],
        c=data["concentration"]
    )
    logging.info("Otput: %s %s", ch.files, ch.validate_csv_header())
    ch.add_constants_to_columns()
