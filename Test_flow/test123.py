import time
for i in range(100):
    time.sleep(1)
    print('dd' + time.strftime('%M.%S', time.localtime(time.time())))