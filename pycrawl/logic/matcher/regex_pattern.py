from pycrawl.logic.matcher.matcher_interface import MatcherInterface


class RegexPattern(MatcherInterface):
    @staticmethod
    def get_matches(text: str, pattern: str) -> int:
        return 0
