# -*-coding:utf-8-*-

import MySQLdb

class Select():
    def SelectData(self,key):
        self.conn = MySQLdb.connect(host="139.196.29.97", db='movie', user='root', passwd='root', port=3306, charset= 'utf8', use_unicode=True)
        self.cur = self.conn.cursor()

        sql = "select %s from best_movies" %key
        self.cur.execute(sql)

        results = self.cur.fetchall()

       # for row in results:
      #      id = row[0]
      #      info = row[1]
	#    url = row[9]
         #   print "%s, %s" %(id, info)
        self.cur.close()
        self.conn.close()
        return results
