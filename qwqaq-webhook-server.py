# encoding: utf-8

import os
from flask import Flask, abort, request
app = Flask(__name__)

HOST = '0.0.0.0'
PORT = 51231
HOOK_ACTIONS = [
    {
        'path': '/qwqaq-git-pull',
        'token': 'test',
        'dir': 'C:/Users/Zneia/WebstormProjects/qwqaqBlog/public',
        'cmd': 'git pull',
    },
]


@app.route('/<path:path>', methods=['GET', 'POST'])
def any_path(path):
    for item in HOOK_ACTIONS:

        if item['path'].lstrip('/') == path.lstrip('/'):
            if request.args.get("token") != item['token']:
                print('*** ACCESS DENIED ***')
                abort(403)

            print('*** AUTO ACTION INITIATED ***')
            os.chdir(item['dir'])
            os.system(item['cmd'])
            print('*** AUTO ACTION COMPLETED ***')

            return '*** AUTO ACTION COMPLETED ***'

    abort(404)


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host=HOST, port=PORT)
