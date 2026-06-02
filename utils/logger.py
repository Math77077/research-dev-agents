import logging
import sys

logger = logging.getLogger("agent_ecosystem")
logger.setLevel(logging.INFO)

if not logger.handlers:
    formatter = logging.Formatter(
        fmt="%(asctime)s | [%(levelname)s] | %(filename)s:%(lineno)d | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    file_handler = logging.FileHandler("debate_system.log", mode="a", encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)