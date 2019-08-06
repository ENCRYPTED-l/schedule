import sqlite3


conn = sqlite3.connect('data.tim', check_same_thread=False)
cur = conn.cursor()

try:
    cur.execute('''CREATE TABLE teachers(teachers text)''')

    cur.execute('''CREATE TABLE subjects(subjects text, hours int)''')

    cur.execute('''CREATE TABLE groups(groups text)''')

    cur.execute('''CREATE TABLE auditory(auditory text)''')


except:
    pass

