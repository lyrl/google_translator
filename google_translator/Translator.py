#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 翻译官
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from google_translator import GoogleConmunication
import Lang


class Translator(object):
    # 翻译
    # @ParamType content string
    # 要翻译的文本
    # @ReturnType string
    def translate(self, content=None):
        if not content:
            return content

        return self.__google_conmunication.translate(source_lang=self.get_source_lang(),
                                                     target_lang=self.get_target_lang(), content=content)

    # @ReturnType string
    def get_target_lang(self):
        return self.__target_lang

    # @ParamType target_lang string
    # @ReturnType void
    def set_target_lang(self, target_lang):
        self.__target_lang = target_lang

    # @ReturnType string
    def get_source_lang(self):
        return self.__source_lang

    # @ParamType source_lang string
    # @ReturnType void
    def set_source_lang(self, source_lang):
        self.__source_lang = source_lang

    def __init__(self, target_lang):
        # @AttributeType string
        # 目标语言
        self.__target_lang = None
        # @AttributeType string
        # 源语言，默认为auto，程序会自动检测语言
        self.__source_lang = "auto"
        # @AttributeType GoogleConmunication
        # 通讯类
        self.__google_conmunication = GoogleConmunication.GoogleConmunication()

        if target_lang:
            self.set_target_lang(target_lang)

if __name__ == "__main__":
    content = sys.argv[1]
    t = Translator(Lang.Lang.chinese_simplified)
    print t.translate(content)