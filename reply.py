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
        self.__dict['picurl_big'] = "http://139.196.29.97:80/images/16175025-e8ae03a3023543a28d9b6be8b03990c9.jpg"
    	self.__dict['url_big'] = "www.baidu.com"
        self.__dict['description_big'] = "历史回顾"
       # self.__dict['description'] = description
    	self.__dict['title_big'] = "histroy"
    #	self.__dict['title'] = title
    	self.__dict['CreateTime'] = int(time.time())
        for i in rang(1,7):
	    self.__dict['title%d'%i] == title[i][0].encode('utf-8')
	    print self.__dict['title%d'%i]
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
        <ArticleCount>7</ArticleCount>
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
	<item>
        <Title><![CDATA[{title6}]]></Title>
        <Description><![CDATA[{description6}]]></Description>
        <PicUrl><![CDATA[{picurl6}]]></PicUrl>
        <Url><![CDATA[{url6}]]></Url>
        </item>
        </Articles>
        </xml> 
        """
        return XmlForm.format(**self.__dict)
