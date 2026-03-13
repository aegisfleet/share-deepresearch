import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))
from fix_bold_brackets import fix_bold_brackets

class TestFixBoldBrackets(unittest.TestCase):
    def test_heading_is_skipped(self):
        content = "# **「テスト」**"
        self.assertEqual(fix_bold_brackets(content), "# **「テスト」**")

        content = "## **「テスト」**\nNormal **「text」**"
        expected = "## **「テスト」**\nNormal <strong>「text」</strong>"
        self.assertEqual(fix_bold_brackets(content), expected)

    def test_replaces_bold_brackets(self):
        content = "**「テスト」**"
        expected = "<strong>「テスト」</strong>"
        self.assertEqual(fix_bold_brackets(content), expected)

        content = "ここは**「重要」**です。"
        expected = "ここは<strong>「重要」</strong>です。"
        self.assertEqual(fix_bold_brackets(content), expected)

    def test_ignores_normal_bold_text(self):
        content = "**重要**"
        expected = "**重要**"
        self.assertEqual(fix_bold_brackets(content), expected)

        content = "ここは**重要**です。"
        expected = "ここは**重要**です。"
        self.assertEqual(fix_bold_brackets(content), expected)

    def test_escaped_asterisks(self):
        content = r"\*\*「テスト」\*\*"
        expected = r"<strong>「テスト」</strong>"
        self.assertEqual(fix_bold_brackets(content), expected)

        content = r"\\**「テスト」\\**"
        expected = r"<strong>「テスト」</strong>"
        self.assertEqual(fix_bold_brackets(content), expected)

    def test_duplicate_cleanup(self):
        content = "<strong>**「テスト」**</strong>"
        expected = "<strong>「テスト」</strong>"
        self.assertEqual(fix_bold_brackets(content), expected)

    def test_newlines_preserved(self):
        content1 = "**「テスト」**\n**「テスト2」**"
        expected1 = "<strong>「テスト」</strong>\n<strong>「テスト2」</strong>"
        self.assertEqual(fix_bold_brackets(content1), expected1)

        content2 = "**「テスト」**\n"
        expected2 = "<strong>「テスト」</strong>\n"
        self.assertEqual(fix_bold_brackets(content2), expected2)

if __name__ == '__main__':
    unittest.main()
