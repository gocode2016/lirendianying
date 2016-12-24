# -*- coding: utf-8 -*-
# filename: main.py
import web
from handle import Handle
from images import Images
from index import Index
from index_new import IndexNew
from history import History
from wearing import Wear
from history_new import HistoryNew
from interface_js import InterfaceJS
urls = (
    '/', 'Handle',
    '/MP_verify_4zXQNL6J5S0J2tmS.txt','InterfaceJS',
    '/images/(.*)', "Images",
    '/index/','Index',
    '/history','History',
    '/history_new','HistoryNew',
    '/index/new', 'IndexNew',
    '/wearing', 'Wear',
)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()

