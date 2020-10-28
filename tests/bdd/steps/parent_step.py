import logging
import os
import unittest

from behave import given


class ParentStep(unittest.TestCase):
    @given("a path to our resources {path}")
    def path_to_resources_step(self, path: str):
        os.environ["TEST_PATH"] = path
        self.path = path
        self.logger = logging.getLogger(__name__)
        self.logger.info(f"Setting up test with resource path: {path}")
