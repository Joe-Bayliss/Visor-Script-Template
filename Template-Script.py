import codecs
import json
import logging
import logging.config
import os

# ----- Variables -----
script_name = "Template"


def setup_logging(config_file):
    # Load the configuration.
    with codecs.open(config_file, "r", encoding="utf-8") as fd:
        config = json.load(fd)

    # Set log filepath
    config["logging"]["handlers"]["log_file"]["filename"] = f"logs/{script_name}.log"

    # Check log folder exists
    if not os.path.exists("logs"):
        os.makedirs("logs")

    # Set up loggers
    logging.config.dictConfig(config["logging"])


def main():
    # Setup logging
    setup_logging("logging.json")
    logger = logging.getLogger()

    # Start script
    logger.info("Script is starting")
    run()


def run():
    # Script goes here
    pass


if __name__ == "__main__":
    main()
