import unittest
import unittest.mock as mock
import os, sys

import project_template


class TestSimpleThings(unittest.TestCase):
    def setUp(self, dao_config, dao_logging, dao_bigquery):
        self.pt = project_template()


if __name__ == "__main__":
    unittest.main()
