from pycrawl.logic.parser.parser_interface import ParserInterface


class Pdf(ParserInterface):
    def get_text(self, file_path: str) -> str:
        pass

    def is_valid(self, file_path: str) -> str:
        pass
