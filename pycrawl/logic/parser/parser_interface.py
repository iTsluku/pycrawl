from abc import ABC, abstractmethod


class ParserInterface(ABC):
    @abstractmethod
    def get_text(self, file_path: str) -> str:
        """The method parses the text of a file, identified by the file path.

        Args:
            file_path (str): File path.

        Returns:
            str: Text of that file.
        """

    @abstractmethod
    def is_valid(self, file_path: str) -> bool:
        """The method checks if the file type matches.

        Args:
            file_path (str): File path.

        Returns:
            bool: True if file type matches class.
        """
