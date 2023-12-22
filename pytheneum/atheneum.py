"""A boilerplate module for Python packate/library design"""

class Atheneum: #pylint:disable=too-few-public-methods
    """The atheneum class has all the answers"""

    def __init__(self) -> None:
        pass

    def answer(self, exclamation):
        """
        Return the answer to Life, the Universe, and Everything.

        :param exclamation:     Print how you feel about the answer
        """

        print(exclamation)
        return 42
