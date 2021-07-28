# -*- coding: utf-8 -*-
from flask import Flask
from RU.server.app import app

def run():
    app.run(host='0.0.0.0', port=8080, debug=True)

if __name__ == '__main__':
    run()