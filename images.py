# -*- coding:utf8 -*-
#file:images

import web

class Images(object):
    def GET(self, name):
	imageBinary = open("/root/git/weixin/lirendianying/images/"+name,'rb').read()
        return imageBinary
    
