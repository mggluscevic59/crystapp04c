import logging

# from crystapp04c.changer import Changer
from crystapp04c.revisor import Revisor, is_csv, extend_csv

# _log = logging.getLogger(__name__)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # 1 & 3 column inserted
    data = {
        "integration"   : 0.0,
        ""              : 0.0,
        "conc"          : 0.0
    }
    # tup:list[tuple[str,float]] = [("integration",0.0),("",0.0),("conc",0.0)]
    # for key, _ in data.items():
    #     data[key] = float(input(f"{key}: "))

    # path = input("File: ")
    # ch = Changer(
    #     path=path,
    #     t=data["integration"],
    #     c=data["concentration"]
    # )
    # logging.info("Otput: %s %s", ch.files, ch.validate_csv_header())
    # ch.add_constants_to_columns()
    rev = Revisor(".test.csv", **data)
    for path in rev.map:
        if path.is_file and is_csv(path):
            extend_csv(path, rev.values)
