#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 与google服务器通讯类
import urllib2
import urllib
from Lang import *

# @ParamType TIME_OUT int
# 默认5秒
TIME_OUT = 5


class GoogleConmunication(object):
    # 发送翻译请求到google服务器，返回翻译的内容
    # @ParamType sourceLang string
    # 源语言
    # @ParamType targetLang string
    # 目标语言
    # @ParamType content string
    # 待翻译的内容
    # @ReturnType string
    def translate(self, source_lang=Lang.auto, target_lang=Lang.chinese_simplified, content=None):
        if not content:
            return content

        data = {"client": "t", "sl": source_lang, "tl": target_lang, "dt": "t", "ie": "UTF-8", "q": content}
        data = urllib.urlencode(data)

        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib2.Request(self.__baseUrl, data, headers)

        raw = urllib2.urlopen(req, timeout=TIME_OUT).read()

        return self.parse_resutlt(raw)

    def parse_resutlt(self, raw=None):
        # 解析服务器返回得信息
        # @ParamType raw string
        # 服务器返回未经解析的数据
        # @ReturnType string
        if not raw:
            return raw

        index = raw.rfind(']],')

        raw = raw[1:index+2] + r''

        result_list = eval(raw)

        result = ''

        for i in result_list:
            result += i[0]

        return result

    def __init__(self):
        # @AttributeType string
        # google翻译接口地址
        self.__baseUrl = "https://translate.google.com/translate_a/single"






