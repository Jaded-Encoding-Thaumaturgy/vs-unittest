import unittest

import vapoursynth as vs

__all__ = [
    'VSTestCase'
]


class VSTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.core = vs.core
