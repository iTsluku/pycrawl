from pycrawl.logic.matcher.matcher_interface import MatcherInterface


class Regex(MatcherInterface):
    def get_matches(self, text: str, query: str) -> int:
        pass
