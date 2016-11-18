# -*-coding:utf-8-*-

import web
   
class Index:
    def GET(self):
        name = 'JasonLeezhi'
        return render.test(name)
