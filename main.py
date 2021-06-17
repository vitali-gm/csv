from classes.db import Db
from datetime import datetime
from threading import Thread

TYPE_NEW = 'new'
TYPE_REPEAT = 'repeat'
TYPE_NEW_MERGE = 'new_merge'
TYPE_REPEAT_MERGE = 'repeat_merge'


db = Db()

def handle(t):

    count = 0

    first_contact = db.one_without_type()

    while first_contact != None:

        print(str(t) + " - " + str(count))

        all_with_contact = db.by_contact(first_contact[3])

        start_rp = all_with_contact[0]

        for i, item in enumerate(all_with_contact):
            db.update_type(TYPE_REPEAT, item[0])
            if start_rp[0] != item[0]:
                item_date = datetime.strptime(item[1], '%d.%m.%Y').date()
                start_rp_date = datetime.strptime(start_rp[1], '%d.%m.%Y').date()
                if start_rp_date > item_date:
                    start_rp = item

        db.update_type(TYPE_NEW, start_rp[0])

        for i, item in enumerate(all_with_contact):
            for j, jtem in enumerate(all_with_contact):
                if item[0] != jtem[0]:
                    i_date = datetime.strptime(item[1], '%d.%m.%Y').date()
                    j_date = datetime.strptime(jtem[1], '%d.%m.%Y').date()

                    if i_date == j_date:
                        if item[4] == TYPE_NEW:
                            db.update_type(TYPE_NEW_MERGE, item[0])
                        else:
                            db.update_type(TYPE_REPEAT_MERGE, item[0])

                        if jtem[4] == TYPE_NEW:
                            db.update_type(TYPE_NEW_MERGE, jtem[0])
                        else:
                            db.update_type(TYPE_REPEAT_MERGE, jtem[0])

        first_contact = db.one_without_type()
        count = count + 1


for i in range(1):
    th = Thread(target=handle, args=(i, ))
    th.start()
