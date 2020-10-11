#!/usr/bin/python3
#0L01019_藤井慶之

import sys
import io
import sqlite3

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
connection = sqlite3.connect("db\\sample.db")
cursor = connection.cursor()


html = """Content-Type: text/html

<html lang="ja">
<head>
  <meta charset="utf-8">
  <title>Web開発 掲示板</title>
  <link href="../css/sample.css" rel="stylesheet">
</head>
<body>
  <div class="header">
    <h1>掲示板</h1>
  </div>

  <div class="main-contain">
    <div class="thread">
      <h2>Test thread</h2>
      {thread}
    </div>

    <form action="form.py" method="post">
      <label for="name">名前</label>
      <input type="text" name="name" value="名無し">
      <input type="submit" value="投稿">
      <p></p>
      <textarea name="article"></textarea>
    </form>
  </div>
</body>
</html>
"""
board = """
<div class="board">
  <dt>名前：{name}　{time}<hr><dd>
  {article}
  <br>
</div>
"""

thread=""

cursor.execute('select * from thread')
for i in cursor.fetchall():
  thread += board.format(name=i[0],time=i[2],article=i[1])

print(html.format(thread=thread))

cursor.close()
connection.close()