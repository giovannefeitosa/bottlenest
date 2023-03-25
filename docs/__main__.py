import os
import sys
from flask import Flask, send_from_directory
import os
from bottlenest.utils.FileUtils import FileUtils


def run():
    app = Flask(__name__)
    distHtmlDir = FileUtils.absPath('dist-docs/html')
    print("distHtmlDir = ", distHtmlDir)

    @app.route('/')
    def serve_home():
        return send_from_directory(
            distHtmlDir,
            'index.html',
        )

    @app.route('/<path:path>')
    def serve_docs(path):
        print(path)
        return send_from_directory(
            distHtmlDir,
            path,
        )
    # @app.route('/<path:path>')

    def run_server():
        app.run()

    print(os.getcwd())
    run_server()


def build():
    # sys.path.insert(0, os.path.abspath('src/bottlenest'))
    # os.system("sphinx-build -b html docs dist-docs")
    os.system("rm -rf dist-docs")
    os.system("make -C docs html")
