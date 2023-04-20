import os
import time

data_folder = '/data'

while True:
    for filename in os.listdir(data_folder):
        with open(data_folder + '/' + filename, 'r') as f:
            print(f'Filename: {filename} - Content: {f.read()}')
    time.sleep(10)

