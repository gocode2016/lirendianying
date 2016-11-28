# -*-coding:utf-8-*-

import MySQLdb

class SelectDaily():
    row = ()
    def GetData(self):
        global row
        conn = MySQLdb.connect(host="139.196.29.97", db='movie', user='root', passwd='root', port=3306,
                                    charset='utf8', use_unicode=True)
        cur = conn.cursor()
        cur.execute('SELECT * FROM new_movies')
        numrow = int(cur.rowcount)
        print numrow
        if numrow == 0:
            print "there is not raw in new_movies"
            cur.close()
            conn.close()

        while True:
            row = cur.fetchone()
            if row[9] != None:
                break;
	try:
            del_col_sql = "DELETE FROM new_movies WHERE movie_name='%s'" %row[0]
            cur.execute(del_col_sql)
        except MySQLdb.Error, e:
            print "Mysql Error %d : %s" %(e.args[0], e.args[1])
        conn.commit()
        cur.close()
        conn.close()
        print row
        return row

    def Insert(self):
        global row
        conn = MySQLdb.connect(host="139.196.29.97", db='movie', user='root', passwd='root', port=3306,
                               charset='utf8', use_unicode=True)
        cur = conn.cursor()
        sql = 'INSERT INTO old_new_movies(movie_name, movie_rate, movie_direct,movie_writer,movie_roles,movie_language,movie_date\
                ,movie_long,movie_description,movie_url,movie_id,movie_picurl)\
               VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        param = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
        cur.execute(sql, param)
        conn.commit()
        cur.close()
        conn.close()

if __name__ == '__main__':
    test = SelectDaily()
    print test.GetData()[0].encode('UTF8')
    test.Insert()

