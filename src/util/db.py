import psycopg2
from util import globals
from util import formatter

# Docs: https://pypi.python.org/pypi/simplemysql
# http://pythonhosted.org/psycopg2/usage.html

# insert(), update(), delete(), getOne(), getAll(), query()
cur = globals.db_conn.cursor()
con = globals.db_conn

#SELECT * from rangesearch WHERE current_timestamp - interval '30 minutes' < last_update

# Inserts a single record into a table.
def insert(table, row_d):
    keys = row_d.keys()
    values = formatter.dict_to_listvalues(row_d)
    SQL = "INSERT INTO %s (%s) VALUES (%s)" % (table, ",".join(row_d.keys()),
                                               ",".join(values))
    cur.execute(SQL)
    con.commit()


# Update one more or rows based on a condition (or no condition).
def update(table, row_d, where_d):
    pass


# Insert a new row, or update if there is a primary key conflict.
def insertOrUpdate(table, row_d, key):
    pass


def selectAll(table, fields_l):
    SQL = "Select %s from %s" % (",".join(fields_l), table)
    cur.execute(SQL)
    return cur.fetchall()


def delete(table, condition_l):
    pass


def query(qry):
    pass
