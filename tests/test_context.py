import unittest
from unittest import mock
import os
from atlas.context import Context, camel_case_spaced, lower_snake_case


class TestContext(unittest.TestCase):
    def test_camel_case_spaced(self):
        self.assertEqual("Sample APp Pro", camel_case_spaced("SampleAPpPro"))

    def test_lower_snake_case(self):
        self.assertEqual("sample_app_pro", lower_snake_case(None, "SampleAPpPro"))

    @mock.patch.dict(
        os.environ, {"SUPER_ARGS": "mytemp", "USER_NAME": "bob"}, clear=True
    )
    def test_context_compiliation(self):
        ctx = Context(args={"super_args": "right_answer", "verbose": False})
        self.assertEqual(ctx["user_name"], "bob")
        self.assertEqual(ctx["super_args"], "right_answer")
        self.assertEqual(ctx["verbose"], False)
        self.assertEqual(ctx.env["SUPER_ARGS"], "mytemp")
