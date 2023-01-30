import os


def lower_snake_case(key):
    """input string is updated to be lower snake case"""
    return key


class Context(dict):
    """
    Context is a special dictionary class for maintianing a operating set of parameters that can be passed through
    multiple App classes.
    """

    # By default all keys will be reduced to lower_snake_case
    key_renamer = lower_snake_case

    def init(self, args=None):
        self.args = args
        self.env = os.environ
