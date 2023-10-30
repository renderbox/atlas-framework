import unittest

from unittest import mock
import sys
from atlas.app import App
from atlas.mixins.unreal import UnrealAppMixin

# Mock the library here
sys.modules["unreal"] = mock.Mock()


class UnrealSampleApp(UnrealAppMixin, App):
    pass


class TestMayaMixin(unittest.TestCase):
    # Test the MayaMixin App to make sure the host is set properly

    def setUp(self) -> None:
        super().setUp()
        self.app = UnrealSampleApp()

    def test_determine_host(self):
        self.assertEqual(self.app.host, "unreal")
