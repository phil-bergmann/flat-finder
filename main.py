import argparse

from flat_finder import Processor
from dotenv import load_dotenv
import sys
import os


def soup():
    parser = argparse.ArgumentParser(
        prog='ProgramName',
        description='What the program does',
        epilog='Text at the bottom of help')
    parser.add_argument("--config_path", default="./config")
    args = parser.parse_args()
    config_path = args.config_path
    load_dotenv(f"{config_path}/.env")
    p = Processor(config_path)
    p.run()

if __name__ == "__main__":
    soup()