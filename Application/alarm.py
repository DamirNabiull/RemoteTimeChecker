import time
import readers
import logging

logging.basicConfig(filename='Logs/app_timer.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def alarm_clock(threadName):
    while True:
        time.sleep(120)
        readers.read_time()
        readers.read_players()
        print(readers.time_d)
        if time.strftime('%H') == readers.time_d['start']:
            for i in readers.players_d:
                # wakeonlan by i

            time.sleep(120)
        elif time.strftime('%H') == readers.time_d['end']:
            for i in readers.players_d:
                # send sleep by readers.players_d[i]

            time.sleep(120)

        print(time.strftime('%H'), time.strftime('%M'))
