from typing import Sequence
import argparse


def main(arguments: Sequence[str] = None):
    '''The main entrypoint for the program.
    '''

    parser = argparse.ArgumentParser(__name__)
    namespace = parser.parse_args(arguments)
    print(namespace)
