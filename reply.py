# -*- coding: utf-8 -*-
# filename: reply.py
import time

class Msg(object):
    def __init__(self):
        pass
    def send(self):
        return "success"

class TextMsg(Msg):
    def __init__(self, toUserName, fromUserName, content):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Content'] = content
       # print "fffffffffffffff"
    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{Content}]]></Content>
        </xml>
        """
        return XmlForm.format(**self.__dict)
    
class ImageMsg(Msg):
    def __init__(self, toUserName, fromUserName, mediaId):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['MediaId'] = mediaId
    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[image]]></MsgType>
        <Image>
        <MediaId><![CDATA[{MediaId}]]></MediaId>
        </Image>
        </xml>
        """
        return XmlForm.format(**self.__dict)



class ImageTextMsg(Msg):
    def __init__(self, toUserName, fromUserName, title, description, picurl, url):
        self.__dict = dict()
        self.__dict['toUser'] = toUserName
        self.__dict['fromUser'] = fromUserName
        self.__dict['picurl_big'] = "http://139.196.29.97:80/images/2169762_103947888000_2.jpg"
        self.__dict['url_big'] = "http://benjen.win/index/movie.html"
        self.__dict['description_big'] = "历史回顾"
        self.__dict['title_big'] = "histroy"
        self.__dict['CreateTime'] = int(time.time())
        print self.__dict['description_big']
        for i in range(1,6):
            self.__dict['title%d'%i] = title[i][0].encode('utf-8')
            self.__dict['picurl%d' %i] = picurl[i][0].encode('utf-8')
            self.__dict['url%d' %i] = url[i][0].encode('utf-8')
            self.__dict['description%d' %i] = description[i][0].encode('utf-8')
    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{toUser}]]></ToUserName>
        <FromUserName><![CDATA[{fromUser}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[news]]></MsgType>
        <ArticleCount>6</ArticleCount>
        <Articles>
        <item>
        <Title><![CDATA[{title_big}]]></Title> 
        <Description><![CDATA[{description_big}]]></Description>
        <PicUrl><![CDATA[{picurl_big}]]></PicUrl>
        <Url><![CDATA[{url_big}]]></Url>
        </item>
        <item>
        <Title><![CDATA[{title1}]]></Title>
        <Description><![CDATA[{description1}]]></Description>
        <PicUrl><![CDATA[{picurl1}]]></PicUrl>
        <Url><![CDATA[{url1}]]></Url>
        </item>
        <item>
        <Title><![CDATA[{title2}]]></Title>
        <Description><![CDATA[{description2}]]></Description>
        <PicUrl><![CDATA[{picurl2}]]></PicUrl>
        <Url><![CDATA[{url2}]]></Url>
        </item>
        <item>
        <Title><![CDATA[{title3}]]></Title>
        <Description><![CDATA[{description3}]]></Description>
        <PicUrl><![CDATA[{picurl3}]]></PicUrl>
        <Url><![CDATA[{url3}]]></Url>
        </item>
        <item>
        <Title><![CDATA[{title4}]]></Title>
        <Description><![CDATA[{description4}]]></Description>
        <PicUrl><![CDATA[{picurl4}]]></PicUrl>
        <Url><![CDATA[{url4}]]></Url>
        </item>
        <item>
        <Title><![CDATA[{title5}]]></Title>
        <Description><![CDATA[{description5}]]></Description>
        <PicUrl><![CDATA[{picurl5}]]></PicUrl>
        <Url><![CDATA[{url5}]]></Url>
        </item>
        </Articles>
        </xml> 
        """
        return XmlForm.format(**self.__dict)
