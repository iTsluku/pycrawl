import enum
import logging


@enum.unique
class ReturnCode(enum.IntEnum):
    """Return codes for pypong."""

    OK = 0
    """Successful execution with expected ending."""

    SETUP_FAILED = 1
    """Execution failed in the setup phase."""


logging.basicConfig(
    format="%(asctime)s [%(levelname)s] (%(name)s:%(funcName)s:%(lineno)d): %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def main(argv) -> int:
    # TODO setup
    logger.info("Setup env.")
    # TODO parse argv
    logger.info("Parse input arguments.")
    return ReturnCode.OK
