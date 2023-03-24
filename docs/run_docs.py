from flask import Flask, send_from_directory
import os


def main():
    app = Flask(__name__)

    @app.route('/')
    def serve_home():
        return send_from_directory('../dist-docs', 'index.html')

    @app.route('/<path:path>')
    def serve_docs(path):
        print(path)
        return send_from_directory('../dist-docs', path)
    # @app.route('/<path:path>')

    def run_server():
        app.run()

    print(os.getcwd())
    run_server()
