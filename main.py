from flat_finder import Processor
from dotenv import load_dotenv
import os

from flat_finder.adapters import SlackAdapter


def soup():
    load_dotenv()
    p = Processor()
    p.run()

if __name__ == "__main__":
    soup()