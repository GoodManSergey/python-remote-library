from flask import Flask
from flask import request
from flask import jsonify
from remote.remote_class import RemoteClass


class RemoteServer(object):

    def __init__(self, host, port, rm_lib):
        self.__host = host
        self.__port = port
        self.__remote_class = RemoteClass(rm_lib)

    def serve_forever(self):
        app = Flask("remote_lib")

        @app.route("/", methods=['POST'])
        def use_class():
            content = request.get_json()

            method = content["method"]
            args = tuple(content["args"])
            kwargs = content["kwargs"]

            data = self.__remote_class.call_method(method, *args, **kwargs)

            return jsonify(data)

        app.run(host=self.__host, port=self.__port)
