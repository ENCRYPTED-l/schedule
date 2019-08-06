from infinity_iterator import *
import random
from selector import *


def shedule_builder():

    teachers, auditories, subjects, hours, groups = select()

    subjects = dict(zip(subjects, hours))
    print(subjects)

    days = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]

    dayz = ListCollection(days)
    itr = dayz.iterator()
    day, subj, spd = [], [], []

    check, total = {}, []

    for g in groups:
        print (g)
        subj.clear()
        day.clear()
        for x in range(7):
            itr.next()
            day.append(itr.current())
            spd.clear()
            for i in range(3): # Допустим 3 пары в день, либо можно указать в зависимости от дня
                try:
                    current_subj = random.choice(list(subjects))
                    spd.append(current_subj)
                    if subjects[current_subj] == 0:
                        subjects.pop(current_subj)
                    else:
                        subjects[current_subj] = subjects[current_subj] - 1
                except:
                    break
            subj.extend(spd)



        y, out = 0, []



        for x in (day):
            out.append('------------------------------------------------')
            out.append(x)
            out.extend(subj[y:y + 3])
            check[x] = subj[y:y+3]
            y += 3

        print(check)

        total = total + out



    return total

shedule_builder()


