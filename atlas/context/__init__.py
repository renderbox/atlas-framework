import os
import re

camel_case_split_regex = re.compile(
    "([a-z])([A-Z])"
)  # Compiled for running over lots of keys


def camel_case_spaced(key):
    return camel_case_split_regex.sub(r"\1 \2", key)


def lower_snake_case(instance, key):
    """input string is updated to be lower snake case

    * Note; since this called like a method in the instance, it needs to have an extra 'instance' argument (aka 'self')
    """
    return camel_case_split_regex.sub(r"\1_\2", key).lower()


class Context(dict):
    """
    Context is a special dictionary class for maintianing a operating set of parameters that can be passed through
    multiple App classes.
    """

    # By default all keys will be reduced to lower_snake_case
    key_renamer = lower_snake_case
    config_parser = None
    include_env = True

    def __init__(self, args=None, config=None, *pargs, **kwargs):
        super().__init__(*pargs, **kwargs)
        print("Generating Context")
        self.parse_config(config)
        self.parse_env()
        self.parse_args(args)

    def parse_config(self, config):
        """
        Provides a check to handle case where there is no parser set.
        """
        if self.config_parser:
            self.config = self.config_parser(config)
            self.update_context(**self.config)
        else:
            self.config = None

    def parse_env(self):
        """Parses the environment and updates the context with values."""
        self.env = os.environ
        # print(self.env)
        if self.env and self.include_env:
            self.update_context(**self.env)

    def parse_args(self, args):
        self.args = args
        if self.args:
            self.update_context(**self.args)

    def update_context(self, **kwargs):
        """Updates the context with values and renames the key."""
        for key in kwargs:
            self[self.key_renamer(key)] = kwargs[key]
