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
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text' and recMsg.Content == '1':
                mysqlData = mysql.Select()
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                results_name = mysqlData.SelectData("movie_name","old_movies")
                results_url = mysqlData.SelectData("movie_url","old_movies")
                results_rate = mysqlData.SelectData("movie_rate","old_movies")
                results_pic = mysqlData.SelectData("movie_picurl","old_movies")
                url_big = "http://alitiane.com/history"
                title_big = "点击进入经典电影观看目录"
                replyMsg = reply.ImageTextMsg(toUser, fromUser,results_name, results_rate, results_pic,results_url,url_big,title_big)
                return replyMsg.send()
            
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text' and recMsg.Content == '2':
                mysqlData = mysql.Select()
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                results_name = mysqlData.SelectData("movie_name","old_new_movies")
                results_url = mysqlData.SelectData("movie_url","old_new_movies")
                results_rate = mysqlData.SelectData("movie_rate","old_new_movies")
                results_pic = mysqlData.SelectData("movie_picurl","old_new_movies")
                url_big = "http://alitiane.com/history_new"
                title_big = "点击进入热门电影观看目录"
                replyMsg = reply.ImageTextMsg(toUser, fromUser,results_name, results_rate, results_pic,results_url,url_big,title_big)
                return replyMsg.send()

            elif isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text' and recMsg.Content == '3':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                title = "AI围棋"
                content = "天元围棋利用深度学习等人工智能技术，同时允许多人挑战，目前棋力已达业余六段, 点击进入对战..."
                picturl = "http://alitiane.com/images/weiqi.jpg"
                url = "https://ty.tianrang.com"
                replyMsg = reply.ImageTextMsgSimple(toUser, fromUser, title, content, picturl, url)
                return replyMsg.send()
              
            elif isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text' and recMsg.Content == '4':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                title = "餐厅卫生状况查询"
                content = "对接上海市食品药品监督管理局系统信息，提供实时准确的餐饮店家的卫生状况评估，点击进入..."
                picturl = "http://alitiane.com/images/foodcheck.jpg"
                url = "http://shanghaicity.openservice.kankanews.com/public/cy/index"
                replyMsg = reply.ImageTextMsgSimple(toUser, fromUser, title, content, picturl, url)
                return replyMsg.send()
            elif isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text' and recMsg.Content == '5':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                title = "公交实时查询"
                content = "对接上海市公交系统信息，提供实时准确的公交车到站时间查询，点击进入..."
                picturl = "http://alitiane.com/images/buscheck.jpg"
                url = "http://139.196.29.97:8080"
                replyMsg = reply.ImageTextMsgSimple(toUser, fromUser, title, content, picturl, url)
                return replyMsg.send()
            
            elif isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                tempSql = mysql.Select()
                #content_sm = "回复‘1’：经典电影观看\n\r回复‘2’：最新电影观看\n\r回复‘3’：挑战AI围棋\n\r回复‘4’：上海餐厅卫生状况查询\n\r回复其它字符：使用说明"
                name = recMsg.Content
                if not name:
                    content_sm = "回复‘1’：经典电影观看\n\r回复‘2’：最新电影观看\n\r回复‘3’：挑战AI围棋\n\r回复‘4’：上海餐厅卫生状况查询\n\r 输入电影名查询电影"
                    replyMsg = reply.TextMsg(toUser, fromUser, content_sm)
                    return replyMsg.send()
                else:
                    result = tempSql.QueryMovies(name)
                    if not result:
                        content_sm = "sorry, %s还没加入到库里，我们会尽快加入"%name
                        replyMsg = reply.TextMsg(toUser, fromUser, content_sm)
                    else:
                        #print result[0][0]
                        #print result[0][8]
                        #print result[0][11]
                        #print result[0][9]
                        replyMsg = reply.ImageTextMsgSimple(toUser, fromUser, result[0][0].encode('utf8'), result[0][8].encode('utf8'), result[0][11], result[0][9])
                return replyMsg.send()


            elif recMsg.MsgType == 'event':
                if recMsg.Event == "subscribe":
                    toUser = recMsg.FromUserName
                    fromUser = recMsg.ToUserName
                    content_sm = "每日推送最好最新的电影 \n\r 回复‘1’：观看经典电影\n\r 回复‘2’：观看最新电影\n\r 回复‘3’：挑战AI围棋\n\r 回复‘4’：上海餐厅卫生状况查询\n\r 回复其它字符：使用说明"
                    title = "丽人电影欢迎您          --阿狸天鹅出品"
                    temp = mysql.Select()
                    movie = temp.GetDataOld()
                    picturl = movie[11]
                    replyMsg = reply.ImageTextMsgSimple(toUser, fromUser, title, content_sm, picturl, "http://alitiane.com/index/")
                    return replyMsg.send()
                if recMsg.Event == "unsubscribe":
                    toUser = recMsg.FromUserName
                    fromUser = recMsg.ToUserName
                    content_sm = "很抱歉，没达到您的预期，我们会继续努力改进"
                    replyMsg = reply.TextMsg(toUser, fromUser, content_sm)
                    return replyMsg.send()
            else:
                print "暂且不处理"
                return "success"

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

