import unittest
from ..scraper import Scraper


class TestScrapper(unittest.TestCase):
    def setUp(self) -> None:
        self.scrapper = Scraper()
