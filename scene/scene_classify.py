#!/usr/bin env python
# import sys
# sys.path.append('/Users/chris/PycharmProjects/code-ysu-python/excel/parse_excel.py')
# sys.path.append('/Users/chris/PycharmProjects/code-ysu-python/http/parse_scene_by_http.py')
#
# from parse_scene_by_http import classify_queries
# from parse_excel import load_data_from_excel
import openpyxl
import json
import urllib2
import urllib
import traceback
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
all_count = 0
spliter = ' '


def load_data_from_excel(path):
    wb = openpyxl.load_workbook(path)
    sheet = wb['Sheet1']
    query = []
    for item in list(sheet.rows)[1:]:
        query.append(item[0].value)

    wb.close()
    return query


def parse_json_in_str(data):
    # parse json and convert everything from unicode to str
    return json.loads(data)


def classify_queries(query_array):
    classify_result = []
    for query in query_array:
        try:
            encoded_query = urllib.quote(query.encode('utf8'))
        except BaseException:
            print 'query %s exception' % (query)
        # seller_id = title2seller[1]
        url_template = 'https://alibee-shop.taobao.org/alibee/intention.htm?q=%s' % (encoded_query)
        request_result = {}
        try:
            request_result = classify_query(url_template)
            classify_result.append(request_result)
        except BaseException:
            print 'url_template has a problem:' + url_template
            traceback.print_exc()
    return classify_result


def classify_query(url):
    #print url
    global all_count
    all_count += 1
    req = urllib2.Request(url)
    fd = urllib2.urlopen(req)

    jsonObj = {}
    data = fd.read()
    # print data
    if (data != 'null'):
        jsonObj = parse_json_in_str(data)

    request_result = {}
    if jsonObj:
        request_result = {'question': str(jsonObj.get('question')), 'scene': str(jsonObj.get('sceneKey')),
                          'packName': str(jsonObj.get('packName'))}

    return request_result

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
