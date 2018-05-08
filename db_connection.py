import pymysql as mysql
import json
import db_sqls as sqls


def connectDB():
    host = 'felipexlr50.mysql.pythonanywhere-services.com'
    user = 'felipexlr50'
    pwd = '6X6ds8486x'
    database = 'felipexlr50$rpg'

    # db = mysql.connect(host, user, pwd, database)
    db = mysql.connect('localhost', 'root', '', 'rpg')
    return db


def initDatabase():
    db = connectDB()
    cursor = db.cursor()
    sqlList = sqls.getSqls()
    for sql in sqlList:

        sql = sql.replace('\n', '')
        sql = sql.replace('`', '')

        try:
            print(sql)
            cursor.execute(sql)
            db.commit()

        except Exception as e:
            print(e)
            db.rollback()

    db.close()


initDatabase()


def getBaseSelect(table, args):
    result = ''
    if(args['fields']):
        fields = args['fields']
        sqlInit = "SELECT " + str(fields) + " FROM "+str(table)
    else:
        sqlInit = "SELECT * FROM " + str(table)

    if(args['condition']):
        condition = " "+str(args['condition'])
        return sqlInit + condition
    else:
        return sqlInit


def getUpdateArgs(args, table, id):
    sqlInit = "UPDATE "+str(table)+" SET "
    sqlSet = ",".join(str(arg['name']) + " = " +
                      "'"+str(arg['value'])+"'" for arg in args)

    sqlCondition = "WHERE id = "+str(id)
    return sqlInit + sqlSet + sqlCondition


def getInsertArgs(table, args):
    sqlInit = "INSERT INTO "+str(table)
    sqlInto = ",".join(str(arg['name']) for arg in args)
    sqlValues = ",".join("'"+str(arg['value'])+"'" for arg in args)

    return sqlInit + "(" + sqlInto + ") VALUES("+sqlValues+")"


def update(id, args, table):
    db = connectDB()
    cursor = db.cursor()
    sql = getUpdateArgs(args, table, id)
    result = None
    try:
        cursor.execute(sql)
        db.commit()
        result = True
    except Exception as e:
        print(e)
        db.rollback()
        result = False
    finally:
        return result


def insert(table, args):
    db = connectDB()
    cursor = db.cursor()
    sql = getInsertArgs(table, args)
    result = None
    try:
        cursor.execute(sql)
        db.commit()
        result = True
    except Exception as e:
        print(e)
        db.rollback()
        result = False
    finally:
        return result


def select(table, args):
    db = connectDB()
    cursor = db.cursor()
    sql = getBaseSelect(table, args)
    results = ''
    fieldNames = ''

    try:
        cursor.execute(sql)
        fields = len(cursor.description)
        fieldNames = [i[0] for i in cursor.description]
        results = cursor.fetchall()
    except Exception as e:
        results = False
        print(e)
    finally:
        return results, fieldNames
    db.close()


def getMapTables(interface):

    if interface == "users":
        return "user"
    elif interface == "players":
        return "player"
    elif interface == "quests":
        return "quest"
    elif interface == "items":
        return "item"
    elif interface == "sessions":
        return "session"
    elif interface == "masters":
        return "master"
    elif interface == "skills":
        return "skill"
    elif interface == "npcs":
        return "npc"
    else:
        return None
