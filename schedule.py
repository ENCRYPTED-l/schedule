from flask import *
from dbs import *
from builder import *




# conn = connection to dbs ------- cur = cursor --- cur.execute - actions

app = Flask(__name__)


@app.route('/')
def index():
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
    return render_template('bound.html', teachers = teachers, subjects = subjects, hours_ = hours_, auditories = auditories, groups = groups)

#                               ------------------ЗАПОЛНЕНИЕ БД--------------------



@app.route('/', methods=['POST'])
def my_form_post():

    print(shedule_builder())

    teacher = request.form['teacher']
    subject = request.form['subject']
    hours = request.form['hours']
    auditory = request.form['auditory']
    group = request.form['group']
    teacher = (teacher,)
    subj = (subject, hours)
    auditory = (auditory,)
    group = (group,)


    if teacher[0] != '':
        cur.execute('''INSERT INTO teachers(teachers) VALUES (?)''', teacher)
    if subject != '' or hours != '':
        cur.execute('''INSERT INTO subjects(subjects, hours) VALUES(?,?)''', subj)
    if auditory[0] != '':
        cur.execute('''INSERT INTO auditory(auditory) VALUES(?)''', auditory)
    if group[0] != '':
        cur.execute('''INSERT INTO groups(groups) VALUES(?)''', group)

    conn.commit()


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


    return render_template('bound.html', teacher=teacher, subject=subject, hours=hours, auditory=auditory, group=group,
                           teachers=teachers, subjects=subjects, hours_=hours_, auditories=auditories, groups=groups)



#                      ------SCHEDULER-------
@app.route('/schedule.html')
def schedule():
    out = shedule_builder()
    return render_template('schedule.html', out = out)







if __name__ == "__main__":
    app.run()
