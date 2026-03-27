import unittest
import tempfile
import os
import sys
from unittest.mock import patch
from datetime import datetime

# Add scripts directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts')))

from format_citations import format_citations_in_file

class TestFormatCitations(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_file_path = os.path.join(self.temp_dir.name, 'test.md')

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_valid_date(self):
        content = """---
title: Test
date: 2023-10-05
---
#### **引用文献**
Citations: 1. Example Title, http://example.com
"""
        with open(self.temp_file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        format_citations_in_file(self.temp_file_path)

        with open(self.temp_file_path, 'r', encoding='utf-8') as f:
            result = f.read()

        self.assertIn("10月 5, 2023にアクセス", result)
        self.assertIn("1. Example Title, 10月 5, 2023にアクセス、 [http://example.com](http://example.com)", result)

    @patch('format_citations.datetime')
    def test_invalid_date_fallback(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2024, 1, 15)
        # We need strptime to actually fail with ValueError
        mock_datetime.strptime.side_effect = ValueError

        content = """---
title: Test
date: invalid-date
---
#### **引用文献**
Citations: 1. Example Title, http://example.com
"""
        with open(self.temp_file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        format_citations_in_file(self.temp_file_path)

        with open(self.temp_file_path, 'r', encoding='utf-8') as f:
            result = f.read()

        self.assertIn("1月 15, 2024にアクセス", result)

    @patch('format_citations.datetime')
    def test_missing_date_fallback(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2024, 1, 15)

        content = """---
title: Test
---
#### **引用文献**
Citations: 1. Example Title, http://example.com
"""
        with open(self.temp_file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        format_citations_in_file(self.temp_file_path)

        with open(self.temp_file_path, 'r', encoding='utf-8') as f:
            result = f.read()

        self.assertIn("1月 15, 2024にアクセス", result)

if __name__ == '__main__':
    unittest.main()
