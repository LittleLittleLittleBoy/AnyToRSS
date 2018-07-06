# -*- coding: utf-8 -*-


class RssDocument(object):
    def __init__(self, title, url=''):
        self.__title = title
        self.__url = url
        self.__collect = []

    def getHtml(self):

        itemStr='<item></item>'

        if len(self.__collect)!=0:
            itemStr=''
            for item in self.__collect:
                itemStr=itemStr+item.toString()

        return '<?xml version="1.0" encoding="utf-8" ?>\n' \
                 '<rss version="2.0">' \
                 '<channel>' \
                 '<title>'+self.__title+'</title>' \
                 '<link>'+self.__url+'</link>' \
                 '<description>小百合就业</description>' +itemStr +'\n'\
                 '</channel>' \
                 '</rss>'

    def insertItem(self, item):
        self.__collect.append(item)


class Item(object):
    def __init__(self, title, link, content):
        self.title = title
        self.link = link
        self.content = content

    def toString(self):
        return '<item>' \
                '<title> <![CDATA['+self.title+']]> </title>' \
                '<link> <![CDATA['+self.link+']]> </link>' \
                '<description> <![CDATA['+self.content+']]> </description>' \
                '</item>'
