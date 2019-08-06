from dbs import *

def select():
    cur.execute('''SELECT teachers FROM teachers''')
    teachers = cur.fetchall()
    teachers = [x[0] for x in teachers]

    cur.execute("SELECT subjects FROM subjects")
    subjects = cur.fetchall()
    subjects = [x[0] for x in subjects]

    cur.execute('''SELECT hours FROM subjects''')
    hours_ = cur.fetchall()
    hours_ = [x[0] for x in hours_]

    cur.execute('''SELECT auditory FROM auditory''')
    auditories = cur.fetchall()
    auditories = [x[0] for x in auditories]

    cur.execute('''SELECT groups FROM groups''')
    groups = cur.fetchall()
    groups = [x[0] for x in groups]


    return teachers, auditories, subjects, hours_, groups