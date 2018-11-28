# coding: utf-8
from datetime import datetime
import sqlite3
import os


def main():
    connect_sqlite()


def connect_sqlite():
    time = datetime.now().strftime('%H%M%S')
    date = datetime.now().strftime('%Y-%m-%d')
    conn = sqlite3.connect('../db.sqlite3')
    cursor = conn.cursor()
    for item in cursor.execute('''SELECT * FROM rec_radiko_reserve WHERE start_date '''):
        if item[2] == date and item[3][0:2] == time[0:2] and int(time[2:4]) - int(item[3][3:5]) < 1:
            print(os.system('bash ../rec_radiko.sh' + ' ' + item[1] + ' ' + item[4] + ' ' + '../out/'))


if __name__ == '__main__':
    main()
