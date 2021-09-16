import time
import traceback
from concurrent.futures import ThreadPoolExecutor
from parse_scene_by_http import classify_query
from urllib import parse
import sys

sys.path.append("..")
from excel import parse_excel


def parse_scene_in_multi_thread_mode(queries):
    count = 0
    futures = []
    with ThreadPoolExecutor(20) as executor:
        for query in queries:
            try:
                count += 1
                url_template = 'https://alibee-shop.taobao.org/alibee/intention.htm?q=%s' % parse.quote(
                    str(query).encode('utf8'))
                future = executor.submit(classify_query, url_template)
                futures.append(future)
            except BaseException:
                print('query %s exception' % (query))
                traceback.print_exc()
            if count % 100 == 0:
                print('count %d' % count)
    return futures


if __name__ == "__main__":
    start_time = time.time()
    print('start evaluating %s' % str(start_time))
    queries = parse_excel.load_data_from_excel("../data/guangyun_test_query.xlsx")
    futures = parse_scene_in_multi_thread_mode(queries[1:3])

    print('task submitted, start execute task')
    scene_results = []
    error_count = 0
    for future in futures:
        try:
            scene_results.append(future.result())
        except BaseException:
            error_count += 1

    print('task executed, start to write file')
    with open('output.csv', 'a+') as output_file:
        for result in scene_results:
            output_file.write('%s,%s,%s\n' % (result.get('question'), result.get('scene'), result.get('packName')))

    end_time = time.time()
    print('finished, evaluating cost %d, error count %d' % (end_time - start_time, error_count))
