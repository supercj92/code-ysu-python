# coding=utf-8

import parse_excel
import unittest

class ExcelTest(unittest.TestCase):
    '''测试parse_excel'''

    def test_load_data_from_excel(self):
        queries = parse_excel.load_data_from_excel('../data/guangyun_test_query.xlsx')
        print len(queries)
        self.assertEqual(50000, len(queries), 'size not match')

    unittest.main()