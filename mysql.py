# -*-coding:utf-8-*-

import MySQLdb

class Select():
    def SelectDataDesc(self,key, table):
        conn = MySQLdb.connect(host="139.196.29.97", db='movie', user='root', passwd='root', port=3306, charset= 'utf8', use_unicode=True)
        cur = conn.cursor()

        sql = "select %s from %s order by movie_id desc" %(key,table)
        cur.execute(sql)

        results = cur.fetchall()
        cur.close()
        conn.close()
        return results

    def SelectData(self,key, table):
        conn = MySQLdb.connect(host="139.196.29.97", db='movie', user='root', passwd='root', port=3306, charset= 'utf8', use_unicode=True)
        cur = conn.cursor()

        sql = "select %s from %s order by movie_id desc" %(key,table)
        cur.execute(sql)

        results = cur.fetchall()
        cur.close()
        conn.close()
        return results

    def GetDataOld(self):
        conn = MySQLdb.connect(host="139.196.29.97", db='movie', user='root', passwd='root', port=3306,
                                    charset='utf8', use_unicode=True)
        cur = conn.cursor()
        cur.execute('SELECT * FROM old_movies order by movie_id desc')
        numrow = int(cur.rowcount)
        print numrow
        if numrow == 0:
            print "there is not raw in best_movies"
            cur.close()
            conn.close()
            return
        while True:
            row = cur.fetchone()
            if row[9] != None:
                break;
        cur.close()
        conn.close()
        print row
        return row

    def GetDataOldNew(self):
        conn = MySQLdb.connect(host="139.196.29.97", db='movie', user='root', passwd='root', port=3306,
                                    charset='utf8', use_unicode=True)
        cur = conn.cursor()
        cur.execute('SELECT * FROM old_new_movies order by movie_id desc')
        numrow = int(cur.rowcount)
        print numrow
        if numrow == 0:
            print "there is not raw in new_movies"
            cur.close()
            conn.close()
            return
        while True:
            row = cur.fetchone()
            if row[9] != None:
                break;
        cur.close()
        conn.close()
        print row
        return row
