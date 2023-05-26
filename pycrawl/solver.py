import os

from typing import List, Tuple, Optional


def get_relevant_files(args: dict) -> Optional[List[str]]:
    directory_paths: List[str] = args["paths"]
    file_types: Tuple[str] = tuple(args["types"])
    limit: int = args["limit"]
    matcher: str = args["matcher"]

    for directory_path in directory_paths:
        for file in os.scandir(directory_path):
            file_path: str = file.path
            if not file_path.endswith(file_types):
                continue
            # get text
            if file_path.endswith(".pdf"):
                pass
            elif file_path.endswith(".txt"):
                pass
            # get matches + map to file
    # sort matches
    # return matches, given limit
    return None
