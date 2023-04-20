import time

data_folder = '/data'

while True:
    filename = time.strftime('%Y%m%d-%H%M%S') + '.txt'
    with open(data_folder + '/' + filename, 'w') as f:
        f.write(time.strftime('%Y-%m-%d %H:%M:%S'))
    time.sleep(10)

