import os
import textract

from typing import List, Tuple

from pycrawl.logic.matcher.regex_pattern import RegexPattern
from pycrawl.logic.matcher.string_equality_match import StringEqualityMatch


def get_relevant_files(args: dict) -> List[Tuple[float, str]]:
    # TODO docstring: Return list of max <limit> (score,file_path) tuples ordered by score
    directory_paths: List[str] = args["paths"]
    file_types: Tuple[str] = tuple(args["types"])
    limit: int = args["limit"]
    # methods <- one of ("eq_match", "re_pattern")

    for directory_path in directory_paths:
        for file in os.scandir(directory_path):
            file_path: str = file.path
            if not file_path.endswith(file_types):
                continue
            # parse text
            text: str = textract.process(file_path, encoding="ascii").decode("ascii")
            # get matches
            matches: int = 0
            if "eq_match" in args:
                matches = StringEqualityMatch.get_matches(
                    text=text, match=args["eq_match"]
                )
            elif "re_pattern" in args:
                matches = RegexPattern.get_matches(
                    text=text, pattern=args["re_pattern"]
                )
            # map file and matches
    # sort matches
    # normalize and calculate score
    # return matches, given limit
    return []
