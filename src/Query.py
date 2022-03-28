
import sqlite3

# connection = sqlite3.connect("Anglais/data/allverbs.db")
# cursor = connection.cursor()

""" def adding(verb = list()):
    for i in range(3):
        v = input("")
        past = input("")
        pp = input("")
        verb.append((cursor.lastrowid,v,past,pp))
        print("verb added\n")
    return verb """

""" def inserting(verb = list()):
    for i in range(5):
        v = input("")
        trad = input("")
        verb.append((cursor.lastrowid,v,trad))
        print("verb added\n")
    return verb """



# sql_create = """CREATE TABLE irregularverbs(
#     id_irregular INTEGER PRIMARY KEY AUTOINCREMENT,
#     verb TEXT,
#     past TEXT,
#     pp TEXT
# )"""
# cursor.execute(sql_create)

# sql_create = """CREATE TABLE regularverbs(
#     id_regular INTEGER PRIMARY KEY AUTOINCREMENT,
#     verb TEXT,
#     traduction TEXT
# )"""
# cursor.execute(sql_create)


# sql_select = "SELECT traduction FROM irregularverbs WHERE verb = 'stand'"
# cursor.execute(sql_select)
# res = cursor.fetchall()
# print(res)
# for i in res:
#     print(i)


# sql_alter = "ALTER TABLE regularverbs ADD pastparticiple TEXT"
# cursor.execute(sql_alter)


# sql_insert = "INSERT INTO irregularverbs VALUES(?,?,?,?)"
# cursor.executemany(sql_insert,adding())
# connection.commit()

# sql_insert = "INSERT INTO regularverbs VALUES(?,?,?)"
# cursor.executemany(sql_insert,inserting())
# connection.commit()


# Ref hitady caractère specifique de soloina LIKE ilay =
# cursor.execute("SELECT pp FROM irregularverbs WHERE pp LIKE '%rne'")
# res = cursor.fetchall()
# for i in res:
#     print(i)

# cursor.execute("SELECT * FROM irregularverbs WHERE verb = 'work'")
# print(cursor.fetchone())
# sql = "DELETE FROM irregularverbs WHERE verb = 'work'"
# cursor.execute(sql)
# connection.commit()

# cursor.execute("SELECT traduction FROM regularverbs WHERE verb = 'decrease'")
# print(cursor.fetchone())


# sql_update = "UPDATE regularverbs SET traduction = 'diminuer' WHERE verb = 'decrease'"
# cursor.execute(sql_update)
# connection.commit()

# connection.close()


def is_from(p,*v): # p: past participle, past
    try:
        connection = sqlite3.connect("data/allverbs.db")
        cursor = connection.cursor()
        sql_select = "SELECT {} FROM irregularverbs WHERE verb = ?".format(p)
        cursor.execute(sql_select,v)
        res = cursor.fetchone() 
        connection.close()
        if res == None:
            return v[0]
        return res[0]
    except Exception as e:
        print(e)

def is_equal_to(*v):
    try:
        connection = sqlite3.connect("data/allverbs.db")
        cursor = connection.cursor()
        cursor.execute("SELECT verb FROM irregularverbs WHERE verb = past")
        res = cursor.fetchall()
        connection.close()
        return v in res
    except Exception as e:
        print(e)

def is_verb(*v):
    try:
        connection = sqlite3.connect("data/allverbs.db")
        cursor = connection.cursor()
        cursor.execute("SELECT verb FROM irregularverbs UNION SELECT verb FROM regularverbs")
        res = cursor.fetchall()
        connection.close()
        tmp = (v[0].lower(),)
        return tmp in res
    except Exception as e:
        print(e)
        
def is_in(t,*v): #t :  table source
    try:
        connection = sqlite3.connect("data/allverbs.db")
        cursor = connection.cursor()
        tmp = (v[0].lower(),)
        sql_select = "SELECT traduction FROM {} WHERE verb = ?".format(t)
        cursor.execute(sql_select,tmp)
        res = cursor.fetchone()
        connection.close()
        # print(type(res))
        if res != None:
            return res[0]
        return None
    except Exception as e:
        print(e)
        

""" if __name__ == "__main__":
    print(is_from("past","play"))
    print(is_from("pp","freeze"))
    print(is_equal_to("read"))
    print(is_verb("pRay"))
    print(is_in("irregularverbs","go")) """

