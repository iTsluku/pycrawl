from pycrawl.logic.matcher.matcher_interface import MatcherInterface


class StringEqualityMatch(MatcherInterface):
    @staticmethod
    def get_matches(text: str, match: str) -> int:
        return 0
