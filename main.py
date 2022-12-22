from flat_finder import Processor
from dotenv import load_dotenv
import sys
import os

from flat_finder.adapters import SlackAdapter


def soup():
    config_path = "./config"
    if len(sys.argv) > 1:
        config_path = sys.argv[1]
    load_dotenv(f"{config_path}.env")
    p = Processor(config_path)
    p.run()

if __name__ == "__main__":
    soup()