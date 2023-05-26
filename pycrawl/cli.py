import enum
import logging
import argparse
import os
import copy

from typing import List, Optional


@enum.unique
class ReturnCode(enum.IntEnum):
    """Return codes for pycrawl."""

    OK = 0
    """Successful execution with expected ending."""


logging.basicConfig(
    format="%(asctime)s [%(levelname)s] (%(name)s:%(funcName)s:%(lineno)d): %(message)s",
    level=logging.DEBUG,
)
logger: logging.Logger = logging.getLogger(__name__)


def main(argv: Optional[List[str]]) -> int:
    logger.info("Parse arguments...")
    argv: List[str] = strip_argv(argv)
    parser: argparse.ArgumentParser = get_parser()
    args: argparse.Namespace = parser.parse_args(argv)
    args: argparse.Namespace = replace_args(args)
    logger.debug(args)
    # TODO logic
    return ReturnCode.OK


def strip_argv(argv: Optional[List[str]]) -> List[str]:
    if argv is None:
        logger.warning("Failed to load arguments, set to default.")
        return ["--help"]
    if len(argv) <= 1:
        logger.info("Insufficient number of arguments, set to default.")
        return ["--help"]
    argv_copy: Optional[List[str]] = copy.deepcopy(argv)
    argv_copy.pop(0)  # remove first value (script path) of argv (sys.argv output)
    return argv_copy


def replace_args(args: argparse.Namespace) -> argparse.Namespace:
    args_copy: argparse.Namespace = copy.deepcopy(args)
    if vars(args_copy)["paths"] == ["."]:
        vars(args_copy)["paths"] = [os.getcwd()]
    return args_copy


def get_parser() -> argparse.ArgumentParser:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog="Pycrawl",
        description="The Python command line application Pycrawl enables targeted search for relevant documents based on modern techniques and specified predicates.",
    )
    parser.add_argument(
        "-p",
        "--paths",
        nargs="+",
        required=True,
        help="Set directory paths.",
    )
    parser.add_argument(
        "-t",
        "--types",
        nargs="+",
        default=[".pdf"],
        choices=[".txt", ".pdf"],
        help="Set file types.",
    )
    return parser
