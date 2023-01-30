import unittest

# from atlas.app.cli import CLIApp
from .sample import SampleApp


class TestCLIApp(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.cli = SampleApp()

    def test_default_name(self):
        self.assertEqual(self.cli.app_name, "Sample App")
