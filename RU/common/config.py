# -*- coding: utf-8 -*-
from configparser import ConfigParser

_public = './RU/config/config.ini'

class Config:
    def __init__(self):
        try:
            self.config = ConfigParser()
            self.config.read(_public)
        except Exception as e:
            print(e)

    def getPath(self):
        return (
            self.config['options']['TABLET_MODEL'],
            self.config['options']['CONNECTION_BROWER'],
            self.config['options']['POST_PATH'],
            self.config['options']['POST_IMG_PATH'],
            self.config['options']['DRAWING_PATH']
            )

    def getScriptPath(self):
        return (
            self.config['options']['PYTHON_PATH'],
            self.config['options']['SCRIPT_PATH']
        )