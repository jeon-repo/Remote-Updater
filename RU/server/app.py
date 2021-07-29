# -*- coding: utf-8 -*-
import os
from flask import Flask, request, render_template
from RU.common.config import Config

config = Config()
app = Flask('Remote-Updater', static_folder='RU/client/static/', template_folder='RU/client/templates/')

TABLET_MODEL, CONNECTION_BROWER, POST_PATH, POST_IMG_PATH, DRAWING_PATH = config.getPath()
PYTHON_PATH, SCRIPT_PATH = config.getScriptPath()

@app.route('/')
def main():
    device_info = request.user_agent.string
    if TABLET_MODEL in device_info and CONNECTION_BROWER in device_info:
        return render_template('upload.html')
    else:
        return '<h1>접근 불가, 지정된 기기로만 접근 가능</h1>'

@app.route('/uploadDrawing', methods=['GET', 'POST'])
def upload_drawing():
    if request.method == 'POST':
        try:
            img = request.files['upload_drawing']
            if not_auth_file(img):
                return '''<script>alert("인가되지 않은 파일");location.href='/';</script>'''
            img.save(os.path.join(DRAWING_PATH, img.filename))
            return '''<script>alert("그림 파일 업로드");location.href='/';</script>'''
        except Exception as e:
            return f'<h1>{e}</h1>'

@app.route('/uploadPost', methods=['GET', 'POST'])
def upload_post():
    if request.method == 'POST':
        try:
            md = request.files['upload_post']
            md_path = os.path.join(POST_PATH, md.filename)
            if not_auth_file(md):
                md.save(md_path)

            img = request.files['upload_post_img']
            if img.filename != '':
                img_path = os.path.join(POST_IMG_PATH, md.filename.split('.')[0])
                if not os.path.isdir(img_path):
                    os.mkdir(img_path)
                img_path = os.path.join(img_path, img.filename)
                if not_auth_file(img):
                    return '''<script>alert("인가되지 않은 파일");location.href='/';</script>'''
                img.save(img_path)

            return '''<script>alert("포스팅 파일 업로드");location.href='/';</script>'''
        except Exception as e:
            return f'<h1>{e}</h1>'

@app.route('/script/<method>', methods=['GET'])
def script_run(method):
    try:
        os.system(f'{PYTHON_PATH} {SCRIPT_PATH}/{method}.py')
        return f'''<script>alert("깃헙 {method.upper()}");location.href='/';</script>'''
    except Exception as e:
        return f'<h1>{e}</h1>'

def not_auth_file(file):
    if file.filename.split('.')[-1] not in ['png', 'jpg', 'jpeg', 'md']:
        return True
    else:
        return False