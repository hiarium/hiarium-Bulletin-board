#!/usr/bin/python3
#0L01019_藤井慶之

import sys
import io
import cgi
import datetime
import sqlite3

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
connection = sqlite3.connect("db\\sample.db")
cursor = connection.cursor()

form = cgi.FieldStorage()
try:
  if form["name"].value is not None and form["article"].value is not None:
    name = form["name"].value
    article = form["article"].value.replace('\n','<br>')
    now = datetime.datetime.now()
    now_st=now.strftime("%Y/%m/%d %H:%M:%S")
    cursor.execute('insert into thread(name,article,time) values(?,?,?)',[name,article,now_st])
    connection.commit()
except KeyError:
  pass

cursor.close()
connection.close()

print("Content-type: text/html;\n\n")
print("<meta http-equiv=refresh content=0;URL=sample.py>")