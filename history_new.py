# -*-coding:utf-8-*-

import web
import mysql
import MySQLdb
from setting import MYSQL_USER,MYSQL_PASSWD
render = web.template.render('templates/old_movies/')   


class HistoryNew:
    def GET(self):
        movie = {}
        conn = MySQLdb.connect(host="139.196.29.97", db='movie', user=MYSQL_USER, passwd=MYSQL_PASSWD, port=3306,
                                    charset='utf8', use_unicode=True)
        cur = conn.cursor()
        cur.execute('SELECT * FROM old_new_movies order by movie_id desc')
        numrow = int(cur.rowcount)
        print numrow
        for i in range(0,numrow):
            movie[i] = cur.fetchone()
            #print movie[i][11]
            #print i
            #print movie[i][9]
           # movie[i][9] += "http://"
        #print movie
        return render.history(movie, numrow)
