# -*- coding: utf-8 -*-
# filename: main.py
import web
from handle import Handle
from images import Images
from index import Index

render = web.template.render('templates/')
urls = (
    '/', 'Handle',
    '/images/(.*)', "Images",
    '/index/(.*)','Index'
)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()

