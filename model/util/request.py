# -*- coding: utf-8 -*-
import requests


def getContentFromHTML(url,headers={},encode=''):
    try:
        r = requests.get(url,timeout=30,headers=headers)
        r.raise_for_status()
        if encode=='':
            r.encoding =r.raise_for_status()
        else :
            r.encoding=encode
        return r.text
    except:
        print("")
