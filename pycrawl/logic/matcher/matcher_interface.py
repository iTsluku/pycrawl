from abc import ABC, abstractmethod


class MatcherInterface(ABC):
    @staticmethod
    @abstractmethod
    def get_matches(text: str, query: str) -> int:
        """Calculate the number of matches.

         Args:
            text (str): Search space.
            query (str): Query.

        Returns:
            int: Number of matches of the search query with the text to be checked.
        """
