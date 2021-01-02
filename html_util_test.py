import unittest

import html_util


class TestHtmlUtil(unittest.TestCase):

  def testParseTag(self):
    self.assertEqual(html_util.ParseTag('<foo>abc</foo>', 'foo'), 'abc')
    self.assertIsNone(html_util.ParseTag('<foo>abc</foo>', 'baz'))


if __name__ == '__main__':
  unittest.main()
