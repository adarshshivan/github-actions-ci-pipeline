import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def run():
    unused_variable = 42
    logging.info("Application started")
    logging.info("Performing basic validation logic")
    logging.info("Application completed successfully")


if __name__ == "__main__":
    run()
