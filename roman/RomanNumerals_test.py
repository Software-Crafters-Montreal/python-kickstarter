import unittest

from roman import RomanNumerals


class TestRomanNumerals(unittest.TestCase):

  def test_should_return_the_number_one(self):
    self.assertEqual(RomanNumerals.convert(1), 'I')


if __name__ == '__main__':
  unittest.main()
