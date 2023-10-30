import unittest

from unittest import mock
import sys
from atlas.app import App
from atlas.mixins.maya import MayaAppMixin

# Mock the library here
sys.modules["maya"] = mock.Mock()
sys.modules["maya.cmds"] = mock.Mock()


class MayaSampleApp(MayaAppMixin, App):
    pass


class TestMayaMixin(unittest.TestCase):
    # Test the MayaMixin App to make sure the host is set properly

    def setUp(self) -> None:
        super().setUp()
        # Mock the library here
        self.app = MayaSampleApp()

    def test_determine_host(self):
        self.assertEqual(self.app.host, "maya")
