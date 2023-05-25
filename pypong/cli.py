import enum
import logging
import argparse

from typing import List, Optional


@enum.unique
class ReturnCode(enum.IntEnum):
    """Return codes for pypong."""

    OK = 0
    """Successful execution with expected ending."""


logging.basicConfig(
    format="%(asctime)s [%(levelname)s] (%(name)s:%(funcName)s:%(lineno)d): %(message)s",
    level=logging.DEBUG,
)
logger: logging.Logger = logging.getLogger(__name__)


def main(argv: Optional[List[str]]) -> int:
    logger.info("Parse arguments...")
    argv: List[str] = get_stripped_argv(argv)
    parser: argparse.ArgumentParser = get_parser()
    args: argparse.Namespace = parser.parse_args(argv)
    logger.debug(args)
    # TODO logic
    return ReturnCode.OK


def get_stripped_argv(argv: Optional[List[str]]) -> List[str]:
    if argv is None:
        logger.warning("Failed to load arguments, set to default.")
        return ["--help"]
    if len(argv) <= 1:
        logger.info("Insufficient number of arguments, set to default.")
        return ["--help"]
    argv.pop(0)  # remove first value (script path) of argv (sys.argv output)
    return argv


def get_parser() -> argparse.ArgumentParser:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog="Pypong",
        description="The Python command line application Pypong enables targeted search for relevant documents based on modern techniques and specified predicates.",
        epilog='In Germany we say "Gut Kick!"',
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
