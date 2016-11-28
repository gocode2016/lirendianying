# -*-coding:utf-8-*-

import web
import mysql

render = web.template.render('templates/')   

class IndexNew:
    def GET(self):
        temp = mysql.Select()
	movie = temp.GetDataOldNew()
        name = ('test1','test2')
        return render.daily(movie)
