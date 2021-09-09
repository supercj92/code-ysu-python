#!/usr/bin env python

import sys
from parse_excel import load_data_from_excel
from http.parse_scene_by_http import classify_queries

reload(sys)
sys.setdefaultencoding('utf-8')
all_count = 0
spliter = ' '

def write_to_file(to_path, classify_result_array):
    output_file = open(to_path, 'a+')
    res_str = ''
    count = 0
    total = len(classify_result_array)
    for request_result in classify_result_array:
        question = request_result['question']
        scene = request_result['scene']
        package = request_result['packName']
        res_str = '%s %s %s\n' % (question, scene, package)
        count += 1
        if(count % 5000 == 0):
            print 'writing to file.%d/%d' % (count, total)
        output_file.write(res_str)
    print 'writed query %d' % (count)


if __name__ == '__main__':
    query_array = load_data_from_excel('../data/guangyun_test_query.xlsx')
    sub_query_array = query_array
    #print sub_query_array
    classify_result = classify_queries(sub_query_array)
    write_to_file('./classify_result', classify_result)
    print 'write to file success'
    #print classify_result
