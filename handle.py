# -*- coding: utf-8 -*-
# filename: handle.py

import hashlib
import web
import hashlib
import reply
import receive
import mysql
import json
import urllib2

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
                results_name = mysqlData.SelectData("movie_name","best_movies")
                results_url = mysqlData.SelectData("movie_url","best_movies")
                results_rate = mysqlData.SelectData("movie_rate","best_movies")
                results_pic = mysqlData.SelectData("movie_picurl","best_movies")
                replyMsg = reply.ImageTextMsg(toUser, fromUser,results_name, results_rate, results_pic,results_url)
                print replyMsg.send()
                
                return replyMsg.send()
           # elif isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text' and recMsg.Content == '':

            elif isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                content_sm = "回复‘wq’：历史回顾；\n\r回复其它字符：使用说明"
                replyMsg = reply.TextMsg(toUser, fromUser, content_sm)
                return replyMsg.send()
            elif isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'event':
                print recMsg.Content
                if recMsg.Content == "subscribe":
                    toUser = recMsg.FromUserName
                    fromUser = recMsg.ToUserName
                    content_sm = "欢迎使用‘丽人电影’ \n\r每日推送最好最新的电影 让你好看每一天"
                    replyMsg = reply.TextMsg(toUser, fromUser, content_sm)
                    return replyMsg.send()
                if recMsg.Content == "unsubscribe":
                    toUser = recMsg.FromUserName
                    fromUser = recMsg.ToUserName
                    content_sm = "很抱歉，没达到您的预期，我们会继续努力改进"
                    replyMsg = reply.TextMsg(toUser, fromUser, content_sm)
                    return replyMsg.send()
            else:
                print "暂且不处理"
                return "success"
           # elif isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text' and recMsg.Content == 'sm'

     
        except Exception, Argment:
            return Argment

    def xiaohuangji(ask):
        ask = ask.encode('utf-8')
        enask = urllib2.quote(ask)
        send_headers = {'Cookie':'Filtering=0.0; Filtering=0.0; isFirst=1; isFirst=1; simsimi_uid=50840753; simsimi_uid=50840753; teach_btn_url=talk; teach_btn_url=talk; sid=s%3AzwUdofEDCGbrhxyE0sxhKEkF.1wDJhD%2BASBfDiZdvI%2F16VvgTJO7xJb3ZZYT8yLIHVxw; selected_nc=zh; selected_nc=zh; menuType=web; menuType=web; __utma=119922954.2139724797.1396516513.1396516513.1396703679.3; __utmc=119922954; __utmz=119922954.1396516513.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'}
        baseurl = r'http://www.simsimi.com/func/reqN?lc=zh&ft=0.0&req='
        url = baseurl + enask
        req = urllib2.Requrst(url, headers = send_headers)
        resp = urllib2.urlopen(req)
        reson = json.loads(resp.read())
        return reson

