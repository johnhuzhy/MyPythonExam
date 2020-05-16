import pymysql
import time

"""
MySQLを使う
'apilevel', 'charset', 'connect', 'connections', 'constants', 'converters', 'cursors', 'err', 'escape_dict', 
'escape_sequence', 'escape_string', 'get_client_info', 'install_as_MySQLdb', 'optionfile', 'paramstyle', 
'protocol', 'sys', 'thread_safe', 'threadsafety', 'times', 'util', 'version_info'
"""
def insert_db(cur):
    today = time.strftime('%Y-%m-%d')
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    db_user = 'python'
    db_progarm = 'exec_mysql.py'
    db_duration = '2時間'
    # cur.execute("insert into tb_python(work_day,work_progarm,work_duration,create_user,create_datetime,update_user,update_datetime) \
    #     values(%s,%s,%s,%s,%s,%s,%s)",(today,db_progarm,db_duration,db_user,now,db_user,now))
    cur.execute("insert into tb_python(work_day,work_progarm,work_duration,create_user,update_user) \
    values(%s,%s,%s,%s,%s)",(today,db_progarm,db_duration,db_user,db_user))


def update_db(cur):
    db_user = 'python'
    db_progarm = 'exec_mysql.py'
    db_duration = '2.5時間'
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    cur.execute("update tb_python set work_duration=%s, update_user=%s, update_datetime=%s where serial_no =%s",(db_duration,db_user,now,100))

if __name__ == "__main__":
    conn = pymysql.connect(host='localhost', port=3306, user='test',
                           password='zaq12wsx', db='huzhy', charset='utf8')
    cur = conn.cursor()
    # select
    cur.execute("select * from tb_python")
    print(cur.fetchone())
    for line in cur.fetchall():
        print(line)
    
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("select * from tb_python")
    for line in cur.fetchall():
        print(line['work_progarm'])

    # insert
    # insert_db(cur)

    #update
    update_db(cur)

    cur.close()
    conn.commit()
    conn.close()
