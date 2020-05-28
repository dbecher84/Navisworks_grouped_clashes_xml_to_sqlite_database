


import sqlite3
from sqlite3 import Error


def fill_test_table(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """
    
    sql = ''' INSERT INTO clash_test(id,name)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    return cur.lastrowid

def fill_results_table(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """
    
    sql2 = ''' INSERT INTO clash_results(guid,name,status,test_id,date)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql2, task)
    return cur.lastrowid


