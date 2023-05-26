import enum
import logging
import argparse
import os
import copy

from typing import List, Optional
from pycrawl.solver import get_relevant_files


@enum.unique
class ReturnCode(enum.IntEnum):
    """Return codes for pycrawl."""

    OK = 0
    """Successful execution with expected ending."""

    SETUP_FAILED = 1
    """No relevant documents could be found."""

    RETRIEVAL_FAILED = 2
    """No relevant documents could be found."""


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
    logger.debug(args)

    logger.info("Setup...")
    args_dict: Optional[dict] = setup_args(args)
    if args_dict is None:
        return ReturnCode.SETUP_FAILED

    logger.info("Retrieve relevant files...")
    relevant_files: List[str] = get_relevant_files(args_dict)
    if relevant_files is None:
        return ReturnCode.RETRIEVAL_FAILED

    for i, relevant_file in enumerate(relevant_files):
        logger.info(f"[{i}] {relevant_file}")
    return ReturnCode.OK


def strip_argv(argv: Optional[List[str]]) -> List[str]:
    if argv is None:
        logger.error("Failed to load arguments, set to default.")
        return ["--help"]
    if len(argv) <= 1:
        logger.error("Insufficient number of arguments, set to default.")
        return ["--help"]
    argv_copy: Optional[List[str]] = copy.deepcopy(argv)
    argv_copy.pop(0)  # remove first value (script path) of argv (sys.argv output)
    return argv_copy


def setup_args(args: argparse.Namespace) -> Optional[dict]:
    args_dict: dict = vars(args)
    # check assumptions
    if args_dict is None:
        return None
    if not all(k in args_dict for k in ("paths", "matcher", "types", "limit")):
        return None
    # replace "." path input with current working directory
    if args_dict["paths"] == ["."]:
        args_dict["paths"] = [os.getcwd()]
    directory_paths = []
    # check if directories exist
    for directory_path in args_dict["paths"]:
        if not os.path.isdir(directory_path):
            logger.error(f"Directory {directory_path} does not exist.")
        else:
            directory_paths.append(directory_path)
    if not directory_paths:
        logger.critical(f"No existing directory parsed.")
        return None
    return args_dict


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
        "-m",
        "--matcher",
        default="eq",
        type=str,
        choices=["eq", "re"],
        help="Set matcher technique.",
    )
    parser.add_argument(
        "-t",
        "--types",
        nargs="+",
        default=[".pdf"],
        choices=[".txt", ".pdf"],
        help="Set file types.",
    )
    parser.add_argument(
        "-l",
        "--limit",
        default="10",
        type=int,
        help="Set limit for output.",
    )
    return parser
