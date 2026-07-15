import logging


def get_logger(name):

    logging.basicConfig(
        filename="logs/ingestion.log",
        level=logging.INFO,
        format=
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    return logging.getLogger(name)