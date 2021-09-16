import time


def loop_test():
    count = 0
    start_time = time.time()
    while True:
        count += 1
        if time.time() - start_time > 1:
            break
    print('loop in sec %d' % count)


loop_test()
