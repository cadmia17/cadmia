import unittest
from main import *


class UnitTests(unittest.TestCase):

  def test_image_link(self):
      self.assertEquals(image_link("a+b"), "https://chart.googleapis.com/chart?cht=tx&chl=a+b")
    

