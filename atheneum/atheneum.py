"""A boilerplate module for Python packate/library design"""

class Atheneum: #pylint:disable=R0903
    """The atheneum class has all the answers"""

    def __init__(self): #pylint:disable=C0116
        pass

    def answer(self, exclamation_str):
        """
        Return the answer to Life, the Universe, and Everything.

        :param exclamation_str:     Print how you feel about the answer
        """

        print(exclamation_str)
        return 42
