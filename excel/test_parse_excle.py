# coding=utf-8

import parse_excel

if __name__ == '__main__':
    queryArray = parse_excel.parse_query('../data/guangyun_test_query.xlsx')
    print queryArray[0]