import time
import readers
import logging
import os
import requests

logging.basicConfig(filename='Logs/app_timer.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


def alarm_clock(threadName):
    while True:
        time.sleep(120)
        readers.read_time()
        readers.read_players()
        print(readers.time_d)
        if time.strftime('%H') == readers.time_d['start']:
            for i in readers.players_d:
                cmd = f'wakeonlan {i}'
                os.system(cmd)
            time.sleep(120)
            # time.sleep(10800)
        elif time.strftime('%H') == readers.time_d['end']:
            for i in readers.players_d:
                link = f'http://{readers.players_d[i]}:8080/suspend'
                requests.get(link)
            time.sleep(120)
            # time.sleep(10800)
        print(time.strftime('%H'), time.strftime('%M'))
