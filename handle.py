# -*- coding: utf-8 -*-
# filename: handle.py

import hashlib
import web
import hashlib
import reply
import receive
import mysql

class Handle(object):
    count = 0
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "lirendianying" #请按照公众平台官网\基本配置中信息填写

            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print "handle/GET func: hashcode, signature: ", hashcode, signature
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception, Argument:
            return Argument

    def POST(self):
        try:
            webData = web.data()
            print "Handle Post webdata is ", webData   #后台打日志
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text' and recMsg.Content == 'wq':
		mysqlData = mysql.Select()
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                results_name = mysqlData.SelectData("movie_name")
                results_url = mysqlData.SelectData("movie_url")
		results_rate = mysqlData.SelectData("movie_rate")
		results_pic = mysqlData.SelectData("movie_picurl")
                #for content in results_name:
               # Handle.count += 1
               # if Handle.count == 3:
               #     Handle.count = 0
               # content_gb = "电影名:" + results_name[Handle.count][0].encode('utf-8') + "链接：" + results_url[Handle.count][0].encode('utf-8')
                #replyMsg = reply.TextMsg(toUser, fromUser, content_gb)
               # for movie_name in results_name:
                
	       # replyMsg = reply.ImageTextMsg(toUser, fromUser, 'test', 'test', 'description1', 'description', 'http://139.196.29.97:80/images/16175025-e8ae03a3023543a28d9b6be8b03990c9.jpg', 'www.baidu.com')
                replyMsg(toUser, fromUser, resultes_name, resualts_rate, results_pic, results_url)
		return replyMsg.send()
	    elif isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text' and recMsg.Content == 'sm':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
		content_sm = "回复‘wq’历史回顾；回复‘sm’使用说明"
                replyMsg = reply.TextMsg(toUser, fromUser, content_sm)
                return replyMsg.send()
            else:
                print "暂且不处理"
                return "success"
           # elif isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text' and recMsg.Content == 'sm'


        except Exception, Argment:
            return Argment
